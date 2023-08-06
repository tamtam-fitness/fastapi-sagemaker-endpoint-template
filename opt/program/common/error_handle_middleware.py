from typing import Any

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from . import app_logger


# ref: https://qiita.com/sotaheavymetal21/items/508a458a70962d822cb5
class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """エラーハンドリングをするミドルウェア
    API内で発生したエラーをキャッチして処理を施す
    Args:
        BaseHTTPMiddleware : リクエスト/レスポンスインタフェースに対するASGIミドルウェアを記述するための抽象クラス
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
                    "error_msg": "エラーが発生しました、システム管理者に問い合わせてください",
                },
            )
            # stacktraceも出力する
            app_logger.exception(response)

        return response
