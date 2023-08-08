import logging

import sentry_sdk
from fastapi import FastAPI, Response, status
from sentry_sdk.integrations.logging import LoggingIntegration

from opt.program.common import settings
from opt.program.common.error_handle_middleware import ErrorHandlingMiddleware
from opt.program.scoring_service import ScoringService
from opt.program.word2vec_schema import (
    InvocationRequest,
    InvocationResponse,
    WordSimilarity,
)

sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)
if settings.ENV not in ["local", "test"]:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[sentry_logging],
        environment=settings.ENV,
        traces_sample_rate=1.0,
    )


app = FastAPI(title="Word Similarity API")
app.add_middleware(ErrorHandlingMiddleware)

# model load
ScoringService.get_model()


@app.get("/ping")
def ping(response: Response) -> Response:
    health = ScoringService.get_model()
    response.status_code = status.HTTP_200_OK if health else status.HTTP_404_NOT_FOUND

    return response


@app.post("/invocations", response_model=InvocationResponse)
def transformation(invocation_req: InvocationRequest) -> InvocationResponse:
    result = ScoringService.predict(invocation_req.word)
    word_similarities = []
    if result:
        for word, similarity in result:
            word_similarities.append(WordSimilarity(word=word, similarity=similarity))
    return InvocationResponse(word_similarities=word_similarities)
