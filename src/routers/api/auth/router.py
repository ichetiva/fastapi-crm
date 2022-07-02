from fastapi import APIRouter, Depends, BackgroundTasks, Query, HTTPException
from sqlalchemy.orm import Session

from src.db import get_db
from src.crud import users, tokens
from src.services.mail import send_mail_in_background
from src.services.security import make_token
from src.credentials import DOMAIN
from .schemes import (
    ConfirmLoginResponseScheme,
    LoginRequestScheme,
    LoginResponseScheme
)

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/', response_model=LoginResponseScheme)
async def login(
    db: Session = Depends(get_db),
    *,
    data: LoginRequestScheme,
    background_tasks: BackgroundTasks
):
    """Login; create token for confirm login and send message to email"""

    db_user = users.get_user(db, data.email)
    if not db_user:
        raise HTTPException(404, 'User not found with this email.')
    db_token = make_token(
        db, db_user.id, 'confirm-login'
    )
    send_mail_in_background(
        background_tasks,
        data.email,
        'Go to {} for login!'.format(
            DOMAIN + 'api/auth/?token=' + db_token.token
        )
    )
    return {'status': 'ok', 'message': 'We will send you a message for login!'}


@router.get('/', response_model=ConfirmLoginResponseScheme)
async def confirm_login(
    db: Session = Depends(get_db),
    token: str = Query(None)
):
    """
    Confirm login;
    delete token for confirm-login and create token for session
    """

    db_user = tokens.get_user_by_token(db, token)
    if not db_user:
        raise HTTPException(404, 'Token not found')
    db_confirm_login_token = tokens.get_token(db, token)
    tokens.delete_token(db, db_confirm_login_token)
    db_token = make_token(db, db_user.id, 'session')
    db_user = users.update_last_login_user(db, db_user)
    return {
        'status': 'ok',
        'message': 'Token for session was successful ly created.',
        'token': db_token.token
    }
