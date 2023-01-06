import logging

from fastapi import FastAPI

from api.router import deprected_router as deprecated_api_router
from api.router import router as api_router
from core.logger import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(deprecated_api_router)
    application.include_router(api_router, prefix="/api")

    return application


app = get_application()
