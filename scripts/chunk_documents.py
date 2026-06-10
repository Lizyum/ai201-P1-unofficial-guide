import json
import re
from pathlib import Path

"""
Chunk processed documents for retrieval.

This module converts processed markdown documents into
semantically coherent chunks suitable for embedding and
vector retrieval.

Chunking strategies are customized by source type:

- YouTube transcripts: 180 tokens, 50 overlap
- News transcripts: 180 tokens, 50 overlap
- Student stories: 180 tokens, 50 overlap
- Official resources: 100 tokens, no overlap
- Reddit threads: 100 tokens, 80 overlap

Outputs:
    documents/chunks/chunks.json
    documents/chunks/chunk_stats.json
"""


PROCESSED_DIR = Path("documents/processed")
CHUNKS_OUTPUT = Path("documents/chunks/chunks.json")
STATS_OUTPUT = Path("documents/chunks/chunk_stats.json")


CHUNKING_CONFIG = {
    "youtube_transcript": {"chunk_size": 180, "overlap": 50},
    "news_journal_transcript": {"chunk_size": 180, "overlap": 50},
    "student_story": {"chunk_size": 180, "overlap": 50},
    "newsletter_article": {"chunk_size": 180, "overlap": 50},
    "admission_blog": {"chunk_size": 180, "overlap": 50},

    "official_resource": {"chunk_size": 100, "overlap": 0},

    "reddit_thread": {"chunk_size": 100, "overlap": 80},
}


DEFAULT_CONFIG = {"chunk_size": 150, "overlap": 30}


def extract_metadata_and_content(markdown: str) -> tuple[dict, str]:
    
    """
    Extract metadata and document content from a processed markdown file.

    The processed documents generated during ingestion contain a metadata
    header followed by the main document content. This function parses
    the metadata fields and separates them from the content that will
    eventually be chunked and embedded.

    Args:
        markdown: Full markdown document as a string.

    Returns:
        A tuple containing:
            - metadata: Dictionary containing title, source type,
              organization, URL, and topics.
            - content: Main document text without metadata.
    """

    metadata = {}
    lines = markdown.splitlines()
    content_start = 0

    if lines and lines[0].startswith("# "):
        metadata["title"] = lines[0].replace("# ", "").strip()

    for i, line in enumerate(lines):
        if line.startswith("Source Type:"):
            metadata["source_type"] = line.replace("Source Type:", "").strip()
        elif line.startswith("Organization:"):
            metadata["organization"] = line.replace("Organization:", "").strip()
        elif line.startswith("Source URL:"):
            metadata["url"] = line.replace("Source URL:", "").strip()
        elif line.startswith("Topics:"):
            topics = line.replace("Topics:", "").strip()
            metadata["topics"] = [
                topic.strip() for topic in topics.split(",") if topic.strip()
            ]
        elif line.startswith("## Content") or line.startswith("## Original Post"):
            content_start = i + 1
            break

    content = "\n".join(lines[content_start:]).strip()
    return metadata, content


def get_chunking_config(metadata: dict) -> dict:

    """
    Retrieve chunking parameters based on the document source type.

    Different source types require different chunking strategies.
    Long-form narratives benefit from larger chunks with overlap,
    while structured resource pages can use smaller chunks with
    little or no overlap.

    Args:
        metadata: Metadata dictionary extracted from the document.

    Returns:
        Dictionary containing chunk_size and overlap values.
    """

    source_type = metadata.get("source_type", "")
    return CHUNKING_CONFIG.get(source_type, DEFAULT_CONFIG)


def split_into_sections(text: str) -> list[str]:
    """
    Split a document into semantically meaningful sections.

    Documents are first divided using markdown headings before
    token-based chunking is applied. This helps preserve coherent
    units such as Reddit comments, transcript sections, or webpage
    subsections.

    Args:
        text: Document content without metadata.

    Returns:
        List of document sections.
    """
    sections = re.split(r"\n(?=#{2,4} )", text)
    return [section.strip() for section in sections if section.strip()]


def chunk_section(section: str, chunk_size: int, overlap: int) -> list[str]:
    
    """
    Split a document section into overlapping chunks.

    Chunks are created using a sliding window approach based on
    approximate token counts. Overlap is used to preserve context
    between neighboring chunks.

    Args:
        section: Text section to chunk.
        chunk_size: Maximum number of tokens per chunk.
        overlap: Number of overlapping tokens between chunks.

    Returns:
        List of chunk strings.

    Raises:
        ValueError: If overlap is greater than or equal to chunk size.
    """

    words = section.split()

    if len(words) <= chunk_size:
        return [section]

    if overlap >= chunk_size:
        raise ValueError(
            f"Overlap ({overlap}) must be smaller than chunk size ({chunk_size})."
        )

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))

        if end >= len(words):
            break

        start = end - overlap

    return chunks


def chunk_document(file_path: Path) -> list[dict]:

    """
    Chunk a processed markdown document.

    This function:
        1. Loads a processed markdown document.
        2. Extracts metadata and content.
        3. Selects an appropriate chunking strategy.
        4. Splits content into sections.
        5. Generates chunks while preserving metadata.

    Args:
        file_path: Path to a processed markdown document.

    Returns:
        List of chunk dictionaries containing:
            - chunk_id
            - source_file
            - text
            - token_estimate
            - metadata
    """
    
    markdown = file_path.read_text(encoding="utf-8")
    metadata, content = extract_metadata_and_content(markdown)

    config = get_chunking_config(metadata)
    chunk_size = config["chunk_size"]
    overlap = config["overlap"]

    sections = split_into_sections(content)

    chunks = []
    chunk_index = 0

    for section in sections:
        section_chunks = chunk_section(section, chunk_size, overlap)

        for chunk_text in section_chunks:
            chunks.append({
                "chunk_id": f"{file_path.stem}_{chunk_index}",
                "source_file": str(file_path),
                "text": chunk_text,
                "token_estimate": len(chunk_text.split()),
                "metadata": metadata,
            })
            chunk_index += 1

    return chunks


def chunk_all_documents() -> None:

    """
    Chunk all processed documents and save the results.

    Iterates through every markdown file in the processed documents
    directory, applies source-specific chunking, and stores the
    resulting chunks in a consolidated JSON file.

    Also generates summary statistics describing:
        - Number of chunks per document
        - Source type
        - Chunk size used
        - Overlap used

    Output Files:
        documents/chunks/chunks.json
        documents/chunks/chunk_stats.json
    """

    all_chunks = []
    stats = {}

    for file_path in PROCESSED_DIR.glob("*.md"):
        document_chunks = chunk_document(file_path)
        all_chunks.extend(document_chunks)

        stats[file_path.name] = {
            "num_chunks": len(document_chunks),
            "source_type": document_chunks[0]["metadata"].get("source_type", "")
            if document_chunks else "",
            "chunk_size_used": get_chunking_config(document_chunks[0]["metadata"])["chunk_size"]
            if document_chunks else None,
            "overlap_used": get_chunking_config(document_chunks[0]["metadata"])["overlap"]
            if document_chunks else None,
        }

    CHUNKS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with open(CHUNKS_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    with open(STATS_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    print(f"Saved {len(all_chunks)} chunks to {CHUNKS_OUTPUT}")
    print(f"Saved chunk stats to {STATS_OUTPUT}")


if __name__ == "__main__":
    chunk_all_documents()