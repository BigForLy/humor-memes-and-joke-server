import httpx
import asyncio
from tests.test_requests import default_get_requests


def test_deprecated_joke():
    url: str = 'http://127.0.0.1:8000/joke'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_deprecated_status():
    url: str = 'http://127.0.0.1:8000/status'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_deprecated_stories():
    url: str = 'http://127.0.0.1:8000/stories'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_v1_joke():
    url: str = 'http://127.0.0.1:8000/api/v1/joke'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_v1_status():
    url: str = 'http://127.0.0.1:8000/api/v1/status'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_v1_stories():
    url: str = 'http://127.0.0.1:8000/api/v1/stories'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_v2_joke():
    url: str = 'http://127.0.0.1:8000/api/v2/joke'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_v2_status():
    url: str = 'http://127.0.0.1:8000/api/v2/status'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200


def test_v2_stories():
    url: str = 'http://127.0.0.1:8000/api/v2/stories'

    result: httpx.Response = asyncio.run(default_get_requests(url))
    assert result.status_code == 200
