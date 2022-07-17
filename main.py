from fastapi import FastAPI
from api.router import router as api_router


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(api_router)

    return application


app = get_application()
