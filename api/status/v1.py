from fastapi import APIRouter

from core.const import STATUS_TYPE
from core.services import get_humor, string_replace


router = APIRouter()


@router.get("")
async def status():
    humor = get_humor(STATUS_TYPE)
    return string_replace(humor)
