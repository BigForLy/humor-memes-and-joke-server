from fastapi import APIRouter

from core.const import STORIES_TYPE
from core.services import get_humor, string_replace


router = APIRouter()


@router.get("")
async def stories():
    humor = get_humor(STORIES_TYPE)
    return string_replace(humor)
