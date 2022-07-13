from fastapi import FastAPI
from const import JOKE_TYPE, STATUS_TYPE, STORIES_TYPE

from services import get_humor, string_replace


app = FastAPI()


@app.get("/joke")
async def joke():
    humor = get_humor(JOKE_TYPE)
    return string_replace(humor)


@app.get("/stories")
async def stories():
    humor = get_humor(STORIES_TYPE)
    return string_replace(humor)


@app.get("/status")
async def status():
    humor = get_humor(STATUS_TYPE)
    return string_replace(humor)
