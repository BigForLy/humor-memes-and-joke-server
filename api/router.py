from fastapi import APIRouter

from .app import (
    joke, stories, status
)
from .logged import logged


deprected_router = APIRouter(deprecated=True)

deprected_router.include_router(joke.router, tags=["joke"])
deprected_router.include_router(stories.router, tags=["stories"])
deprected_router.include_router(status.router, tags=["status"])


router = APIRouter()
router.include_router(joke.router_api, tags=["joke"])
router.include_router(stories.router_api, tags=["stories"])
router.include_router(status.router_api, tags=["status"])
router.include_router(logged.router_api, tags=["logged"])
