from sqlalchemy.orm import Session
from app.models.document import DocumentChunk


CATEGORY_KEYWORDS = {
    "baggage": ["baggage", "luggage", "bag", "checked", "cabin"],
    "refund": ["refund", "money back", "reimbursement"],
    "cancellation": ["cancel", "cancellation", "hotel cancellation"],
    "flight_change": ["change flight", "flight change", "date change", "reschedule"],
    "visa": ["visa", "passport", "documents", "entry requirements"],
}


def detect_policy_category(query: str) -> str | None:
    text = query.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return None


def search_policy_chunks(db: Session, query: str, limit: int = 1) -> list[str]:
    """MVP retrieval with category filtering.

    Production upgrade:
    - Generate embeddings for chunks.
    - Store embeddings in pgvector or Chroma.
    - Retrieve by cosine similarity.
    """

    category = detect_policy_category(query)
    chunks = db.query(DocumentChunk).all()

    if category:
        matching_chunks = [
            chunk.chunk_text
            for chunk in chunks
            if f'"category":"{category}"' in chunk.metadata_json
        ]

        if matching_chunks:
            return matching_chunks[:limit]

    query_terms = set(query.lower().split())

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
        "Based on the relevant travel policy: "
        f"{evidence} "
        "Please share your booking reference if you want me to check how this applies to your specific booking."
    )
