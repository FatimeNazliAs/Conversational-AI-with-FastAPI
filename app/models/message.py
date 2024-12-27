from datetime import datetime
from sqlalchemy import func
from app.utils.db import Base  
from sqlalchemy.orm import Mapped, mapped_column


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    is_ai: Mapped[bool] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
