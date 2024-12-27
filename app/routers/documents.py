from typing import List
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.models.document import Document
from app.schemas.documentSchema import DocumentResponseSchema
import os

document_router = APIRouter()


@document_router.post("/documents")
def upload_file(uploaded_file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Check if the uploaded file has the correct extension
        if not uploaded_file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        os.makedirs("uploaded_files", exist_ok=True)

        # Define the file location
        file_location = f"uploaded_files/{uploaded_file.filename}"

        # Save the file
        with open(file_location, "wb+") as file_object:
            file_object.write(uploaded_file.file.read())

        document = upload_document(uploaded_file.filename, file_location, db)

        if type(document) == str:
            return document

        return {
            "info": f"File '{uploaded_file.filename}' saved at '{file_location}'",
            "document": document,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


def upload_document(title, file_path, db):

    existing_document = db.query(Document).filter(Document.title == title).first()
    if existing_document:
        return "The document already exists."
    new_document = Document(is_processed=False, title=title, file_path=file_path)

    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document


@document_router.get("/documents", response_model=List[DocumentResponseSchema])
def get_documents(db: Session = Depends(get_db)):
    all_documents = db.query(Document).all()
    return all_documents


@document_router.delete("/documents/{id}")
def delete_document(id: int, db: Session = Depends(get_db)):
    existing_document = db.query(Document).filter(Document.id == id).first()
    s
    if existing_document:
        db.delete(existing_document)  
        db.commit() 
        return {"status": "Document was deleted"}
    
    raise HTTPException(status_code=404, detail="Document not found")


@document_router.delete("/documents")
def delete_all_documents(db: Session = Depends(get_db)):
    try:
        # Delete all documents
        db.query(Document).delete() 
        db.commit()  
        return {"status": "All documents were deleted"}
    
    except Exception as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
