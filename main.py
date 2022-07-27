from fastapi import FastAPI
from api.router import (
    deprected_router as deprecated_api_router,
    router_v1 as api_router_v1
)


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(deprecated_api_router)
    application.include_router(api_router_v1, prefix='/api')

    return application


app = get_application()
