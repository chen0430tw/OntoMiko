from pydantic import BaseModel

class DivineTextRequest(BaseModel):
    text: str
