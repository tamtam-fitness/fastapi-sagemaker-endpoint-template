import logging

import sentry_sdk
from common import settings
from sentry_sdk.integrations.logging import LoggingIntegration

from src.module.temp_class import TempClass

sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)
if settings.ENV not in ["local", "test"]:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[sentry_logging],
        environment=settings.ENV,
        traces_sample_rate=1.0,
    )

if __name__ == "__main__":
    print(TempClass().add_temp("hello_world_"))
