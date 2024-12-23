from app.utils.db import Base  # Import the Base class
from sqlalchemy.orm import Mapped, mapped_column


class DocumentPage(Base):
    __tablename__ = "documentpage"
    document_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    is_processed: Mapped[bool] = mapped_column(nullable=False)
    page_number: Mapped[int] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
