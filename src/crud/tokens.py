from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.db import Token, User


def create_token(
    db: Session,
    user_id: int,
    type_: str,
    token: str
) -> Token:
    db_token = Token(
        user_id=user_id,
        type_=type_,
        token=token
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def get_user_by_token(
    db: Session,
    token: str
) -> User:
    query = db.query(
        User
    )
    query = query.join(Token)
    return query.filter(
        and_(
            Token.token == token,
            (Token.created_at + timedelta(days=30)) >= datetime.now()
        )
    ).first()


def get_token(
    db: Session,
    token: str
) -> Token:
    return db.query(Token).where(Token.token == token).first()


def delete_token(
    db: Session,
    db_token: Token
):
    db.delete(db_token)
    db.commit()


def delete_not_available_tokens(
    db: Session
):
    query = Token.delete().where(
        Token.created_at + timedelta(days=30) < datetime.now()
    )
    db.execute(query)
    db.commit()
