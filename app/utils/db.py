from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# https://github.com/ArjanCodes/examples/blob/main/2024/sqlalchemy/oop_approach.py


# SQLite database file (stored locally in the project directory)
DATABASE_URL = "sqlite:///./test.db"

# Create database engine
engine = create_engine(DATABASE_URL,  connect_args={"check_same_thread": False})

# represent a workspace for your application to interact with the database.
# autocommit->make sure changes are not automatically saved to db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for models
Base = declarative_base()


def get_db():
    # create a new database session and sends it to the client and the session closes itself when the work is done.
    # This function ensures each request has it’s independent database connections.

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
