from fastapi import APIRouter

from api.stories import v1 as v1_stories
from api.joke import v1 as v1_joke
from api.status import v1 as v1_status


deprected_router = APIRouter(deprecated=True)

deprected_router.include_router(v1_joke.router, tags=["joke"], prefix="/joke")
deprected_router.include_router(v1_stories.router, tags=["stories"], prefix="/stories")
deprected_router.include_router(v1_status.router, tags=["status"], prefix="/status")


router_v1 = APIRouter()
router_v1.include_router(v1_joke.router, tags=["joke"], prefix="/v1/joke")
router_v1.include_router(v1_stories.router, tags=["stories"], prefix="/v1/stories")
router_v1.include_router(v1_status.router, tags=["status"], prefix="/v1/status")
