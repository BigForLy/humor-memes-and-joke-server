from fastapi import APIRouter
from core.const import STORIES_TYPE
from core.services import get_humor, string_replace, get_humor_async


router = APIRouter()


@router.get("/stories")
async def stories():
    humor = get_humor(STORIES_TYPE)
    return string_replace(humor)


router_api = APIRouter()


@router_api.get("/v1/stories")
async def stories():
    humor = get_humor(STORIES_TYPE)
    return string_replace(humor)


@router_api.get("/v2/stories")
async def stories():
    humor = await get_humor_async(STORIES_TYPE)
    return string_replace(humor)
