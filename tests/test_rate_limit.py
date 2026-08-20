# ============================================================
# Rate limit headers
# ============================================================


def test_rate_limit_headers_are_returned(weather_client):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219
    )

    assert response.status_code == 200

    expected_headers = [
        "X-RateLimit-Limit",
        "X-RateLimit-Remaining",
        "X-RateLimit-Reset"
    ]

    for header in expected_headers:

        assert header in response.headers, (
            f"Expected documented rate-limit header "
            f"'{header}' but it was not returned by the API."
        )