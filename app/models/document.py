from app.utils.db import Base  # Import the Base class
from sqlalchemy.orm import Mapped, mapped_column


class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    is_processed: Mapped[bool] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    file_path: Mapped[str] = mapped_column(nullable=False, unique=True)
