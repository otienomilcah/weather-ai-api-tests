def test_free_plan_cannot_access_forecast14(weather_client):
    response = weather_client.get_forecast14(
        lat=-1.2921,
        lon=36.8219
    )

    assert response.status_code == 403, (
        f"Expected 403 for Free-plan access to /v1/forecast14, "
        f"but received {response.status_code}"
    )
    
    