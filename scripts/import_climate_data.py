from datetime import date

from app.db.database import SessionLocal
from app.models.climate_measurement import ClimateMeasurement
from app.services.climate_data.database_loader import save_measurements
from app.services.climate_data.loader import load_csv

dataset = load_csv("data/raw/climate_sample.csv")

measurements = [
    ClimateMeasurement(
        date=date.fromisoformat(row["date"]),
        location=row["location"],
        latitude=float(row["latitude"]),
        longitude=float(row["longitude"]),
        temperature_c=float(row["temperature_c"]),
    )
    for _, row in dataset.iterrows()
]

with SessionLocal() as session:
    save_measurements(session, measurements)

print(f"Imported {len(measurements)} climate measurements.")
