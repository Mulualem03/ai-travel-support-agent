from sqlalchemy.orm import Session
from app.models.document import DocumentChunk


def search_policy_chunks(db: Session, query: str, limit: int = 3) -> list[str]:
    """MVP keyword retrieval.

    Production upgrade:
    - Generate embeddings for chunks.
    - Store embeddings in pgvector or Chroma.
    - Retrieve by cosine similarity.
    """
    query_terms = set(query.lower().split())
    chunks = db.query(DocumentChunk).all()

    scored = []
    for chunk in chunks:
        text = chunk.chunk_text.lower()
        score = sum(1 for term in query_terms if term in text)
        if score > 0:
            scored.append((score, chunk.chunk_text))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for _, chunk in scored[:limit]]


def generate_policy_answer(query: str, chunks: list[str]) -> str:
    if not chunks:
        return (
            "I could not find a specific policy for that question. "
            "I can create a support ticket so a human agent can review it."
        )

    evidence = " ".join(chunks)
    return (
        "Based on the travel policy information I found: "
        f"{evidence} "
        "Please share your booking reference if you want me to check how this applies to your specific booking."
    )
