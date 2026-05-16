from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.document import Document

router = APIRouter()


@router.get("")
def list_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()
