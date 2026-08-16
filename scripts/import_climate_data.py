from app.db.database import SessionLocal
from app.models.climate_measurement import ClimateMeasurement
from app.services.climate_data.database_loader import save_measurements
from app.services.climate_data.ecad_loader import (
    load_ecad_temperature_dataset,
)

dataset = load_ecad_temperature_dataset(
    "data/raw/TG_STAID2759.txt",
    "data/raw/TN_STAID2759.txt",
    "data/raw/TX_STAID2759.txt",
)

measurements = [
    ClimateMeasurement(
        date=row["DATE"].date(),
        location="Berlin-Tempelhof",
        latitude=52.473,
        longitude=13.403,
        mean_temperature_c=float(row["TG"]),
        min_temperature_c=float(row["TN"]),
        max_temperature_c=float(row["TX"]),
    )
    for _, row in dataset.iterrows()
]


with SessionLocal() as session:
    session.query(ClimateMeasurement).delete()

    save_measurements(session, measurements)


print(f"Imported {len(measurements)} measurements.")
