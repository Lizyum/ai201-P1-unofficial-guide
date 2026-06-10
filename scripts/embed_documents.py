import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


CHUNKS_PATH = Path("documents/chunks/chunks.json")
CHROMA_PATH = "documents/embeddings/chroma_db"
COLLECTION_NAME = "fgli_resources"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def flatten_metadata(chunk: dict) -> dict:
    """Convert chunk metadata into ChromaDB-safe metadata fields."""
    metadata = chunk.get("metadata", {})

    return {
        "chunk_id": chunk.get("chunk_id", ""),
        "source_file": chunk.get("source_file", ""),
        "title": metadata.get("title", ""),
        "source_type": metadata.get("source_type", ""),
        "organization": metadata.get("organization", ""),
        "url": metadata.get("url", ""),
        "topics": ", ".join(metadata.get("topics", [])),
        "token_estimate": chunk.get("token_estimate", 0),
    }


def load_chunks() -> list[dict]:
    """Load chunk objects from chunks.json."""
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def embed_and_store_chunks() -> None:
    """Embed chunks with all-MiniLM-L6-v2 and store them in ChromaDB."""
    chunks = load_chunks()

    model = SentenceTransformer(EMBEDDING_MODEL)

    documents = [chunk["text"] for chunk in chunks]
    ids = [chunk["chunk_id"] for chunk in chunks]
    metadatas = [flatten_metadata(chunk) for chunk in chunks]

    embeddings = model.encode(documents).tolist()

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB collection: {COLLECTION_NAME}")


if __name__ == "__main__":
    embed_and_store_chunks()