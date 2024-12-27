from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.schemas.messageSchema import MessageResponseSchema, MessageCreateSchema
from app.models.message import Message
from app.utils.classification import classify_message
from app.utils.weather import get_openAI_weather_response

message_router = APIRouter()


@message_router.post("/messages", response_model=MessageResponseSchema)
def create_message(message: MessageCreateSchema, db: Session = Depends(get_db)):
    new_message = Message(is_ai=False, content=message.content)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    response_type = classify_message(new_message.content)
    if response_type == "weather":
        ai_content = get_openAI_weather_response("New York")
        if not isinstance(ai_content, str):
            ai_content = str(ai_content)
        ai_message = Message(is_ai=True, content=ai_content)
        db.add(ai_message)
        db.commit()
        db.refresh(ai_message)

        return ai_message
    if response_type == "food":
        print("Food processing will be added!")


@message_router.get("/messages", response_model=List[MessageResponseSchema])
def get_messages(db: Session = Depends(get_db)):
    all_messages = db.query(Message).all()
    return all_messages


@message_router.delete("/messages/{id}")
def delete_document(id: int, db: Session = Depends(get_db)):
    existing_message = db.query(Message).filter(Message.id == id).first()

    if existing_message:
        db.delete(existing_message)
        db.commit()
        return {"status": "Document was deleted"}

    raise HTTPException(status_code=404, detail="Document not found")


@message_router.delete("/messages")
def delete_all_messages(db: Session = Depends(get_db)):
    try:
        db.query(Message).delete()
        db.commit()
        return {"status": "All messages were deleted"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
