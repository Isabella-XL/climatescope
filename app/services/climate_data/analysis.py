import pandas as pd
from sqlalchemy.orm import Session

from app.models.climate_measurement import ClimateMeasurement


def calculate_temperature_summary(
    temperatures: list[float],
) -> dict[str, float | int | None]:
    """Calculate basic temperature statistics."""
    if not temperatures:
        return {
            "count": 0,
            "average": None,
            "minimum": None,
            "maximum": None,
        }
    series = pd.Series(temperatures)

    return {
        "count": int(series.count()),
        "average": float(series.mean()),
        "minimum": float(series.min()),
        "maximum": float(series.max()),
    }


def analyze_measurements(
    db: Session,
    location: str | None = None,
) -> dict[str, float | int]:
    """Analyze climate measurements from the database."""
    query = db.query(ClimateMeasurement)

    if location:
        query = query.filter(ClimateMeasurement.location == location)

    measurements = query.all()

    temperatures = [measurement.mean_temperature_c for measurement in measurements]

    return calculate_temperature_summary(temperatures)
