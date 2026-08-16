from app.services.climate_data.ecad_loader import (
    load_ecad_temperature_dataset,
)

dataset = load_ecad_temperature_dataset(
    "data/raw/TG_STAID2759.txt",
    "data/raw/TN_STAID2759.txt",
    "data/raw/TX_STAID2759.txt",
)

print(dataset.head(10))
print()
print(dataset.dtypes)
print()
print(f"Rows: {len(dataset)}")
print()
print("Missing values:")
print(dataset.isna().sum())
