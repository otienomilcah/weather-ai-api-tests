import pytest

from utils.api_client import WeatherAPIClient


@pytest.fixture
def weather_client():
    return WeatherAPIClient()


@pytest.fixture
def invalid_api_client():
    return WeatherAPIClient(
        api_key="invalid_api_key"
    )


@pytest.fixture
def unauthenticated_api_client():
    return WeatherAPIClient(
        api_key=None
    )