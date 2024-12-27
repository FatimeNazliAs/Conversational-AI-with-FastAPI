from pydantic import BaseModel


class DocumentResponseSchema(BaseModel):
    id: int
    title: str
    file_path: str
    is_processed: bool
    
