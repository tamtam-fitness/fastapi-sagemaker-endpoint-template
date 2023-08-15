from typing import Any

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from . import app_logger


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """
    Catch errors that occur in the API and apply processing.
    Args:
        BaseHTTPMiddleware : Abstract class for describing ASGI middleware for request/response interfaces.
    """

    async def dispatch(self, request: Request, call_next: Any) -> Response:
        try:
            # 各エンドポイント内で発生したエラーに関しては
            # HttpExceptionをraiseしFastAPI側でエラーハンドリングをしエラーレスポンスが返るようになっている。
            response: Response = await call_next(request)

        except Exception as e:
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error_code": e.__class__.__name__,
                    "error_msg": "An error has occurred, please contact your system administrator.",
                },
            )
            # Also output stacktrace.
            app_logger.exception(response)

        return response
