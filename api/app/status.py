from fastapi import APIRouter
from core.const import STATUS_TYPE
from core.services import get_humor, string_replace, get_humor_async


router = APIRouter()


@router.get("/status")
async def status():
    humor = get_humor(STATUS_TYPE)
    return string_replace(humor)


router_api = APIRouter()


@router_api.get("/v1/status")
async def status():
    humor = get_humor(STATUS_TYPE)
    return string_replace(humor)


@router_api.get("/v2/status")
async def status():
    humor = await get_humor_async(STATUS_TYPE)
    return string_replace(humor)
