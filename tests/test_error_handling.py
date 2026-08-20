from unittest.mock import Mock, patch


def test_weather_handles_server_error(weather_client):

    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {
        "error": "Internal server error"
    }

    with patch("utils.api_client.requests.get",
               return_value=mock_response):

        response = weather_client.get_weather(
            lat=-1.2921,
            lon=36.8219
        )

    assert response.status_code == 500

    response_body = response.json()

    assert isinstance(response_body, dict)


def test_weather_handles_service_unavailable(weather_client):

    mock_response = Mock()
    mock_response.status_code = 503
    mock_response.json.return_value = {
        "error": "Service unavailable"
    }

    with patch("utils.api_client.requests.get",
               return_value=mock_response):

        response = weather_client.get_weather(
            lat=-1.2921,
            lon=36.8219
        )

    assert response.status_code == 503

    response_body = response.json()

    assert isinstance(response_body, dict)


def test_weather_handles_rate_limit(weather_client):

    mock_response = Mock()
    mock_response.status_code = 429
    mock_response.json.return_value = {
        "error": "Rate limit exceeded"
    }

    with patch("utils.api_client.requests.get",
               return_value=mock_response):

        response = weather_client.get_weather(
            lat=-1.2921,
            lon=36.8219
        )

    assert response.status_code == 429

    response_body = response.json()

    assert isinstance(response_body, dict)