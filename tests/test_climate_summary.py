from unittest.mock import MagicMock

from app.models.climate_measurement import ClimateMeasurement
from app.services.climate_data.analysis import (
    analyze_measurements,
    calculate_temperature_summary,
)


def test_calculate_temperature_summary():
    temperatures = [10.0, 20.0, 30.0]

    result = calculate_temperature_summary(temperatures)

    assert result["count"] == 3
    assert result["average"] == 20.0
    assert result["minimum"] == 10.0
    assert result["maximum"] == 30.0


def test_analyze_measurements():
    measurements = [
        ClimateMeasurement(
            location="Berlin-Tempelhof",
            mean_temperature_c=10.0,
            min_temperature_c=5.0,
            max_temperature_c=15.0,
        ),
        ClimateMeasurement(
            location="Berlin-Tempelhof",
            mean_temperature_c=20.0,
            min_temperature_c=15.0,
            max_temperature_c=25.0,
        ),
    ]

    query = MagicMock()
    query.filter.return_value.all.return_value = measurements

    db = MagicMock()
    db.query.return_value = query

    result = analyze_measurements(
        db,
        location="Berlin-Tempelhof",
    )

    assert result["count"] == 2
    assert result["average"] == 15.0
    assert result["minimum"] == 10.0
    assert result["maximum"] == 20.0


def test_analyze_measurements_with_location():
    measurements = [
        ClimateMeasurement(
            location="Berlin-Tempelhof",
            mean_temperature_c=10.0,
            min_temperature_c=5.0,
            max_temperature_c=15.0,
        ),
        ClimateMeasurement(
            location="Berlin-Tempelhof",
            mean_temperature_c=20.0,
            min_temperature_c=15.0,
            max_temperature_c=25.0,
        ),
    ]

    query = MagicMock()
    query.filter.return_value.all.return_value = measurements

    db = MagicMock()
    db.query.return_value = query

    result = analyze_measurements(
        db,
        location="Berlin-Tempelhof",
    )

    query.filter.assert_called_once()

    assert result["count"] == 2
    assert result["average"] == 15.0


def test_calculate_temperature_summary_empty():
    result = calculate_temperature_summary([])

    assert result["count"] == 0
    assert result["average"] is None
    assert result["minimum"] is None
    assert result["maximum"] is None
