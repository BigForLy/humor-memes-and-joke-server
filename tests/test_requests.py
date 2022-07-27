import sys
import httpx
import asyncio
import time
import warnings


async def default_get_requests(url: str) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        return await client.get(url)


def test_start_page():
    url: str = f'http://127.0.0.1:8000/'

    async def request() -> httpx.Response:
        async with httpx.AsyncClient() as client:
            return await client.get(url)

    result = asyncio.run(request())
    assert result.status_code == 404


def test_standart_requests():
    async def _inner():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        url: str = f'http://127.0.0.1:8000/joke'

        async def standart_requests():
            async with httpx.AsyncClient() as client:
                response: httpx.Response = await client.get(url)
                response.raise_for_status()

        tasks = [standart_requests() for _ in range(10)]

        start = time.time()

        await asyncio.gather(*tasks)

        end = time.time() - start
        print(f'time {end:0.2f} seconds', file=sys.stderr)
        print(f'mean time for 1 request: {end/10:0.2f} seconds')
    asyncio.run(_inner())
    assert True
