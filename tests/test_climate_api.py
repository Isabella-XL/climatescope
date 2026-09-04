from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "ClimateScope API is running!",
    }


def test_get_measurements() -> None:
    response = client.get("/api/v1/climate/measurements")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if data:
        measurement = data[0]

        assert "id" in measurement
        assert "date" in measurement
        assert "location" in measurement
        assert "latitude" in measurement
        assert "longitude" in measurement
        assert "mean_temperature_c" in measurement
        assert "min_temperature_c" in measurement
        assert "max_temperature_c" in measurement


def test_get_measurements_by_location() -> None:
    response = client.get(
        "/api/v1/climate/measurements",
        params={"location": "Berlin-Tempelhof"},
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for measurement in data:
        assert measurement["location"] == "Berlin-Tempelhof"


def test_get_measurements_by_date_range() -> None:
    response = client.get(
        "/api/v1/climate/measurements",
        params={
            "location": "Berlin-Tempelhof",
            "start_date": "2025-12-01",
            "end_date": "2025-12-31",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for measurement in data:
        assert measurement["location"] == "Berlin-Tempelhof"
        assert "2025-12-01" <= measurement["date"] <= "2025-12-31"


def test_get_measurements_invalid_date() -> None:
    response = client.get(
        "/api/v1/climate/measurements",
        params={
            "start_date": "not-a-date",
        },
    )

    assert response.status_code == 422


def test_get_climate_summary() -> None:
    response = client.get(
        "/api/v1/climate/summary",
        params={"location": "Berlin-Tempelhof"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["location"] == "Berlin-Tempelhof"
    assert data["measurement_count"] >= 0


def test_get_climate_summary_all_locations() -> None:
    response = client.get(
        "/api/v1/climate/summary",
    )

    assert response.status_code == 200

    data = response.json()

    assert data["location"] is None
    assert data["measurement_count"] > 0
    assert data["average_temperature_c"] is not None
    assert data["minimum_temperature_c"] is not None
    assert data["maximum_temperature_c"] is not None


def test_forecast() -> None:
    payload = {
        "forecast_date": "2026-08-27",
        "location": "Berlin-Tempelhof",
        "TG_lag_1": 10.0,
        "TN_lag_1": 8.0,
        "TX_lag_1": 12.0,
        "TG_lag_7": 11.0,
        "TG_rolling_7": 10.5,
        "TG_rolling_14": 10.8,
        "day_of_year_sin": 0.5,
        "day_of_year_cos": 0.8,
    }

    response = client.post(
        "/api/v1/climate/forecast",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["location"] == "Berlin-Tempelhof"
    assert data["forecast_date"] == "2026-08-27"
    assert "predicted_temperature_c" in data
    assert isinstance(data["predicted_temperature_c"], float)


def test_forecast_missing_feature() -> None:
    payload = {
        "forecast_date": "2026-08-27",
        "TG_lag_1": 10.0,
        "TN_lag_1": 8.0,
        "TX_lag_1": 12.0,
        "TG_lag_7": 11.0,
        "TG_rolling_7": 10.5,
        "TG_rolling_14": 10.8,
        "day_of_year_sin": 0.5,
        # day_of_year_cos is intentionally missing
    }

    response = client.post(
        "/api/v1/climate/forecast",
        json=payload,
    )

    assert response.status_code == 422


def test_forecast_invalid_feature_type() -> None:
    payload = {
        "forecast_date": "2026-08-27",
        "TG_lag_1": "not-a-number",
        "TN_lag_1": 8.0,
        "TX_lag_1": 12.0,
        "TG_lag_7": 11.0,
        "TG_rolling_7": 10.5,
        "TG_rolling_14": 10.8,
        "day_of_year_sin": 0.5,
        "day_of_year_cos": 0.7,
    }

    response = client.post(
        "/api/v1/climate/forecast",
        json=payload,
    )

    assert response.status_code == 422
