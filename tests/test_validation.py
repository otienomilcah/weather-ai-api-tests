# ============================================================
# Required parameter validation
# ============================================================


def test_weather_missing_latitude(weather_client):

    response = weather_client.get_weather(
        lat=None,
        lon=36.8219
    )

    assert response.status_code == 400, (
        f"Expected 400 when latitude is missing, "
        f"but received {response.status_code}"
    )


def test_weather_missing_longitude(weather_client):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=None
    )

    assert response.status_code == 400, (
        f"Expected 400 when longitude is missing, "
        f"but received {response.status_code}"
    )


def test_weather_missing_both_coordinates(weather_client):

    response = weather_client.get_weather(
        lat=None,
        lon=None
    )

    assert response.status_code == 400, (
        f"Expected 400 when both latitude and longitude "
        f"are missing, but received {response.status_code}"
    )