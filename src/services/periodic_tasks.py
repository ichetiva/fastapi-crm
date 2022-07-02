from datetime import datetime

from fastapi import Depends
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session

from src.crud import tokens
from src.db import get_db


@repeat_every(seconds=60*60*24)  # 1 day
def delete_not_available_tokens_task(
    db: Session = Depends(get_db)
):
    print('Stated at {}'.format(datetime.now()))
    tokens.delete_not_available_tokens(db)
