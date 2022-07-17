from fastapi import APIRouter

from const import STATUS_TYPE
from services import get_humor, string_replace


router = APIRouter()


@router.get("")
async def status():
    humor = get_humor(STATUS_TYPE)
    return string_replace(humor)
