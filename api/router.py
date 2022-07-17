from fastapi import APIRouter

from api import joke, stories, status


router = APIRouter()

router.include_router(joke.router, tags=["joke"], prefix="/joke")
router.include_router(stories.router, tags=["stories"], prefix="/stories")
router.include_router(status.router, tags=["status"], prefix="/status")
