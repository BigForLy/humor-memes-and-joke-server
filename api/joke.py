from fastapi import APIRouter

from core.const import JOKE_TYPE
from core.services import get_humor, string_replace


router = APIRouter()


@router.get("")
async def joke():
    humor = get_humor(JOKE_TYPE)
    return string_replace(humor)
