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


def test_get_measurements_by_location() -> None:
    response = client.get(
        "/api/v1/climate/measurements",
        params={"location": "Berlin"},
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for measurement in data:
        assert measurement["location"] == "Berlin"


def test_get_climate_summary() -> None:
    response = client.get(
        "/api/v1/climate/summary",
        params={"location": "Berlin"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["location"] == "Berlin"
    assert data["measurement_count"] >= 0
