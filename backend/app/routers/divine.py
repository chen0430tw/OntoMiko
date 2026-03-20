from fastapi import APIRouter

from app.schemas.divine import DivineTextRequest
from app.services.divine_service import divine_text_service

router = APIRouter(prefix="/divine", tags=["divine"])

@router.post("/text")
def divine_text(req: DivineTextRequest):
    return divine_text_service(req.text)
