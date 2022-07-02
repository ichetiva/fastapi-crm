from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.credentials import DATABASE_URI

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=Session)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
