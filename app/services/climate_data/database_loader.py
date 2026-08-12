from sqlalchemy.orm import Session

from app.models.climate_measurement import ClimateMeasurement


def save_measurements(
    session: Session,
    measurements: list[ClimateMeasurement],
) -> None:
    """Save climate measurements to the database."""
    session.add_all(measurements)
    session.commit()
