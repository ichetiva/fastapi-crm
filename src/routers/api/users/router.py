from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.db import get_db
from src.crud import users, tokens
from .schemes import (
    UpdateUserRequestScheme,
    UserResponseScheme,
    CreateUserRequestScheme
)

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', response_model=UserResponseScheme)
async def create_user(
    db: Session = Depends(get_db),
    *,
    data: CreateUserRequestScheme
):
    """Create user in database"""

    db_user = users.create_user(
        db,
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name
    )
    return db_user


@router.patch('/', response_model=UserResponseScheme)
async def update_user(
    db: Session = Depends(get_db),
    token: str = Query(None),
    *,
    data: UpdateUserRequestScheme
):
    """Update user; column which available for update: first_name, last_name"""

    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    if data.first_name:
        db_user.first_name = data.first_name
    if data.last_name:
        db_user.last_name = data.last_name
    db_user = users.update_user(db, db_user)
    return db_user
