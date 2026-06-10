import os
from dotenv import load_dotenv
from groq import Groq

from scripts.retrieve import retrieve


load_dotenv()

MODEL_NAME = "llama-3.3-70b-versatile"


def format_context(retrieved_chunks: list[dict]) -> str:
    """Format retrieved chunks into numbered context blocks for the LLM."""
    context_blocks = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        metadata = chunk["metadata"]

        title = metadata.get("title", "Unknown Source")
        source_type = metadata.get("source_type", "")
        url = metadata.get("url", "")
        text = chunk["text"]

        context_blocks.append(
            f"""[Source {i}]
Title: {title}
Source Type: {source_type}
URL: {url}

{text}
"""
        )

    return "\n\n".join(context_blocks)


def format_sources(retrieved_chunks: list[dict]) -> str:
    """Create source list programmatically from retrieved chunks."""
    seen = set()
    sources = []

    for chunk in retrieved_chunks:
        metadata = chunk["metadata"]
        title = metadata.get("title", "Unknown Source")
        url = metadata.get("url", "")
        source_key = (title, url)

        if source_key in seen:
            continue

        seen.add(source_key)

        if url:
            sources.append(f"- {title}: {url}")
        else:
            sources.append(f"- {title}")

    return "\n".join(sources)


def generate_answer(query: str, k: int = 5) -> str:
    """Retrieve relevant chunks and generate a grounded answer with Groq."""
    retrieved_chunks = retrieve(query, k=k)
    context = format_context(retrieved_chunks)

    system_prompt = """
You are a grounded RAG assistant for FGLI student experiences and resources at Northwestern University.

You must answer using ONLY the provided retrieved documents.
Do not use outside knowledge.
Do not invent resources, policies, offices, deadlines, or experiences.
If the retrieved documents do not contain enough information to answer the question, say:
"I don't have enough information on that from the provided documents."

Write in a supportive, clear, and concise tone.
"""

    user_prompt = f"""
Question:
{query}

Retrieved Documents:
{context}

Answer the question using only the retrieved documents.
"""

    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()},
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content.strip()

    fallback = "I don't have enough information on that from the provided documents."

    if fallback.lower() in answer.lower():
        return fallback

    sources = format_sources(retrieved_chunks)

    return f"{answer}\n\n## Sources\n{sources}"


if __name__ == "__main__":
    question = "How can FGLI students find community at Northwestern?"
    print(generate_answer(question))