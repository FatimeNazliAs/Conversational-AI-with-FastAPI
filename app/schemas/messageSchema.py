from pydantic import BaseModel
from datetime import datetime


class MessageCreateSchema(BaseModel):
    content: str


class MessageResponseSchema(BaseModel):
    id: int
    is_ai: bool
    content: str
    timestamp: datetime
