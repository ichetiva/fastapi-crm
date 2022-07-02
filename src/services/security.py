import hashlib
from datetime import datetime

from sqlalchemy.orm import Session

from src.crud import tokens
from src.db import Token


def make_token(
    db: Session, user_id: int, type_: str
) -> Token:
    """Create token for confirm login and session"""

    data = {
        'user_id': user_id,
        'type': type_,
        'created_at': datetime.now()
    }
    token = hashlib.md5(str(data).encode()).hexdigest()
    db_token = tokens.create_token(
        db,
        user_id=user_id,
        type_=type_,
        token=token
    )
    return db_token
