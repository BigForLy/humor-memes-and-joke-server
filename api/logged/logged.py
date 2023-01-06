import logging

from fastapi import APIRouter

from .models import LogExc


logger = logging.getLogger(__name__)

router_api = APIRouter()


@router_api.post("/v1/log_exc")
async def status(a: LogExc):
    logger.error(a.log_exc)
    return {"status": True}
