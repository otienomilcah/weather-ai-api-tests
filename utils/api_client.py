import requests

from config.settings import BASE_URL, API_KEY


class WeatherAPIClient:

    def __init__(self, api_key=API_KEY):
        self.base_url = BASE_URL

        self.headers = {
            "Accept": "application/json"
        }

        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    def get_weather(
        self,
        lat,
        lon,
        days=7,
        ai=True,
        units="metric",
        lang="en"
    ):
        params = {
            "lat": lat,
            "lon": lon,
            "days": days,
            "ai": ai,
            "units": units,
            "lang": lang
        }

        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        return requests.get(
            f"{self.base_url}/v1/weather",
            headers=self.headers,
            params=params,
            timeout=10
        )

    def get_forecast14(self, lat, lon):
        params = {
            "lat": lat,
            "lon": lon
        }

        return requests.get(
            f"{self.base_url}/v1/forecast14",
            headers=self.headers,
            params=params,
            timeout=10
        )