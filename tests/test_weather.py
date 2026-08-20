import pytest


# ============================================================
# Valid coordinates
# ============================================================

@pytest.mark.parametrize(
    "lat, lon",
    [
        (-1.2921, 36.8219),      # Nairobi
        (51.5074, -0.1278),      # London
        (40.7128, -74.0060),     # New York
        (-33.8688, 151.2093),    # Sydney
    ]
)
def test_weather_for_valid_coordinates(
    weather_client,
    lat,
    lon
):

    response = weather_client.get_weather(
        lat=lat,
        lon=lon
    )

    assert response.status_code == 200

    response_body = response.json()

    assert isinstance(response_body, dict)

# response_time = response.elapsed.total_seconds()

# assert response_time < 2, (
#    f"Response time was {response_time:.2f}s, "
#        f"exceeding the 2s SLA"
#    )


# ============================================================
# Forecast days
# ============================================================

@pytest.mark.parametrize(
    "days",
    [1, 7]
)
def test_weather_valid_forecast_days(
    weather_client,
    days
):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219,
        days=days
    )

    assert response.status_code == 200

    response_body = response.json()

    assert isinstance(response_body, dict)


# ============================================================
# AI parameter
# ============================================================

@pytest.mark.parametrize(
    "ai",
    [True, False]
)
def test_weather_ai_parameter(
    weather_client,
    ai
):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219,
        ai=ai
    )

    assert response.status_code == 200

    response_body = response.json()

    assert isinstance(response_body, dict)


# ============================================================
# Supported units
# ============================================================

@pytest.mark.parametrize(
    "units",
    ["metric", "imperial"]
)
def test_weather_supported_units(
    weather_client,
    units
):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219,
        units=units
    )

    assert response.status_code == 200

    response_body = response.json()

    assert isinstance(response_body, dict)


# ============================================================
# Supported languages
# ============================================================

@pytest.mark.parametrize(
    "lang",
    ["en", "sw"]
)
def test_weather_supported_languages(
    weather_client,
    lang
):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219,
        lang=lang
    )

    assert response.status_code == 200

    response_body = response.json()

    assert isinstance(response_body, dict)