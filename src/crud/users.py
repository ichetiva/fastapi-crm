from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Session

from src.db import User


def create_user(
    db: Session,
    email: str,
    first_name: str,
    last_name: Optional[str] = None
) -> User:
    db_user = User(
        email=email.lower(),
        first_name=first_name,
        last_name=last_name,
        last_login_at=None
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(
    db: Session,
    email: str
) -> User:
    return db.query(User).where(User.email == email.lower()).first()


def update_user(
    db: Session,
    db_user: User
) -> User:
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_last_login_user(
    db: Session,
    db_user: User
) -> User:
    db_user.last_login_at = datetime.now()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
