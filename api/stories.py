from fastapi import APIRouter

from const import STORIES_TYPE
from services import get_humor, string_replace


router = APIRouter()


@router.get("")
async def stories():
    humor = get_humor(STORIES_TYPE)
    return string_replace(humor)
