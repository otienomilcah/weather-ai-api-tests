# ============================================================
# Valid API key
# ============================================================


def test_valid_api_key(weather_client):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219
    )

    assert response.status_code == 200


# ============================================================
# Invalid API key
# ============================================================


def test_invalid_api_key(invalid_api_client):

    response = invalid_api_client.get_weather(
        lat=-1.2921,
        lon=36.8219
    )

    assert response.status_code == 401, (
        f"Expected 401 for invalid API key, "
        f"but received {response.status_code}"
    )

    response_body = response.json()

    assert isinstance(response_body, dict)


# ============================================================
# Missing API key
# ============================================================


def test_missing_api_key(unauthenticated_api_client):

    response = unauthenticated_api_client.get_weather(
        lat=-1.2921,
        lon=36.8219
    )

    assert response.status_code == 401, (
        f"Expected 401 when API key is missing, "
        f"but received {response.status_code}"
    )


# ============================================================
# Authorization header validation
# ============================================================


def test_valid_api_key_is_sent(weather_client):

    assert "Authorization" in weather_client.headers

    assert weather_client.headers["Authorization"].startswith(
        "Bearer "
    )


def test_missing_api_key_is_not_sent(
    unauthenticated_api_client
):

    assert "Authorization" not in (
        unauthenticated_api_client.headers
    )