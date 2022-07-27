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


async def performance_test(url: str, n_count: int = 10):
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    async def standart_requests():
        response: httpx.Response = await default_get_requests(url)
        response.raise_for_status()

    tasks = [standart_requests() for _ in range(n_count)]

    start = time.time()

    await asyncio.gather(*tasks)

    end = time.time() - start
    print(f'{url = }')
    print(f'time {end:0.2f} seconds')
    print(f'mean time for 1 request: {end/10:0.2f} seconds')


def test_performance_test_v1():
    asyncio.run(performance_test(url=f'http://127.0.0.1:8000/api/v1/joke'))
    # mean time for 1 request: 0.22 seconds
    assert True


def test_performance_test_v2():
    asyncio.run(performance_test(url=f'http://127.0.0.1:8000/api/v2/joke'))
    # mean time for 1 request: 0.06 seconds
    assert True
