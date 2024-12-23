from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# https://github.com/ArjanCodes/examples/blob/main/2024/sqlalchemy/oop_approach.py


# SQLite database file (stored locally in the project directory)
DATABASE_URL = "sqlite:///./conversational_ai_with_fastapi.db"

# Create database engine
engine = create_engine(
    # SQLite-specific flag
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for models
Base = declarative_base()


def get_db():
    """
    Dependency function to get the database session.
    This will be used in FastAPI dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
