# ============================================================
# Single request response time
# ============================================================

def test_weather_response_time(weather_client):

    response = weather_client.get_weather(
        lat=-1.2921,
        lon=36.8219
    )

    assert response.status_code == 200

    response_time = response.elapsed.total_seconds()

    assert response_time < 2, (
        f"Response time was {response_time:.3f}s, "
        f"exceeding the 2-second SLA"
    )


# ============================================================
# Multiple requests performance
# ============================================================

def test_weather_multiple_requests_performance(weather_client):

    response_times = []

    for _ in range(5):

        response = weather_client.get_weather(
            lat=-1.2921,
            lon=36.8219
        )

        assert response.status_code == 200

        response_times.append(
            response.elapsed.total_seconds()
        )

    average_response_time = (
        sum(response_times) / len(response_times)
    )

    maximum_response_time = max(response_times)

    print(
        f"\nAverage response time: "
        f"{average_response_time:.3f}s"
    )

    print(
        f"Maximum response time: "
        f"{maximum_response_time:.3f}s"
    )

    assert average_response_time < 2, (
        f"Average response time was "
        f"{average_response_time:.3f}s, "
        f"exceeding the 2-second SLA"
    )


# ============================================================
# Request success rate
# ============================================================

def test_weather_request_success_rate(weather_client):

    total_requests = 5
    successful_requests = 0

    for _ in range(total_requests):

        response = weather_client.get_weather(
            lat=-1.2921,
            lon=36.8219
        )

        if response.status_code == 200:
            successful_requests += 1

    success_rate = successful_requests / total_requests

    print(
        f"\nSuccess rate: {success_rate:.0%}"
    )

    assert success_rate == 1.0, (
        f"Expected 100% success rate, "
        f"but received {success_rate:.0%}"
    )