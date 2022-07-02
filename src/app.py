from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError


def create_app() -> FastAPI:
    app_ = FastAPI(
        docs_url='/'
    )
    _include_routers(app_)
    _include_exception_handlers(app_)
    _include_periodic_tasks(app_)

    return app_


def _include_routers(app_: FastAPI):
    """Include one router which include all need routers"""

    from src.routers.router import router

    app_.include_router(router)


def _include_exception_handlers(app_: FastAPI):
    """Include exception handlers"""

    from src.exceptions.handler import (
        http_exception_handler,
        integrity_error_handler
    )

    app_.add_exception_handler(HTTPException, http_exception_handler)
    app_.add_exception_handler(IntegrityError, integrity_error_handler)


def _include_periodic_tasks(app_: FastAPI):
    """Include periodic task which delete not available tokens"""

    from src.services.periodic_tasks import delete_not_available_tokens_task

    app_.add_event_handler('startup', delete_not_available_tokens_task)


app = create_app()
