from datetime import datetime

from app.utils.db import Base  # Import the Base class
from sqlalchemy.orm import Mapped, mapped_column
from app.utils.db import Base

class Message(Base):
    __tablename__ = "messages"

     
    id :Mapped[int]= mapped_column(primary_key=True, index=True)
    is_ai: Mapped[bool]= mapped_column(nullable=False)
    content : Mapped[str]= mapped_column( nullable=False)
    timestamp :Mapped[datetime]= mapped_column(nullable=False)

