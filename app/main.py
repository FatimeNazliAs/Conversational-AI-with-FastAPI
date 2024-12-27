from app.utils.db import Base, engine
from fastapi import FastAPI
from app.routers.messages import message_router
from app.routers.documents import document_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(message_router, prefix="/api")
app.include_router(document_router, prefix="/api")
