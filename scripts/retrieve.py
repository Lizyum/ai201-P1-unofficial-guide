import chromadb
from sentence_transformers import SentenceTransformer


CHROMA_PATH = "documents/embeddings/chroma_db"
COLLECTION_NAME = "fgli_resources"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def retrieve(query: str, k: int = 5) -> list[dict]:
    """Retrieve the top-k most relevant chunks for a query."""
    model = SentenceTransformer(EMBEDDING_MODEL)
    query_embedding = model.encode(query).tolist()

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    retrieved_chunks = []

    for i in range(len(results["documents"][0])):
        retrieved_chunks.append({
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i],
        })

    return retrieved_chunks


if __name__ == "__main__":
    test_query = "What are some common experiences as a FGLI at Northwestern University?"

    results = retrieve(test_query, k=6)

    for i, result in enumerate(results, start=1):
        print(f"\n--- Result {i} ---")
        print(f"Title: {result['metadata'].get('title')}")
        print(f"Source Type: {result['metadata'].get('source_type')}")
        print(f"Source File: {result['metadata'].get('source_file')}")
        print(f"Distance: {result['distance']}")
        print(result["text"][:700])