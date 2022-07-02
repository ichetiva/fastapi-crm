from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


async def integrity_error_handler(
    _: Request, exc: HTTPException
) -> JSONResponse:
    response = JSONResponse(
        content={
            'status': 'error',
            'message': 'User with this email already exists.'
        },
        status_code=409
    )
    return response


async def http_exception_handler(
    _: Request, exc: HTTPException
) -> JSONResponse:
    response = JSONResponse(
        content={
            'status': 'error',
            'message': exc.detail
        },
        status_code=exc.status_code
    )
    if exc.headers is not None:
        response.init_headers(exc.headers)

    return response
