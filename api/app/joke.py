from fastapi import APIRouter
from core.const import JOKE_TYPE
from core.services import get_humor, string_replace, get_humor_async


router = APIRouter()


@router.get("/joke")
async def joke():
    humor = get_humor(JOKE_TYPE)
    return string_replace(humor)


router_api = APIRouter()


@router_api.get("/v1/joke")
async def joke():
    humor = get_humor(JOKE_TYPE)
    return string_replace(humor)


@router_api.get("/v2/joke")
async def joke():
    humor = await get_humor_async(JOKE_TYPE)
    return string_replace(humor)
