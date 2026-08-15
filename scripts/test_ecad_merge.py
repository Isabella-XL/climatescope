from app.services.climate_data.ecad_loader import load_ecad_temperature

tg = load_ecad_temperature(
    "data/raw/TG_STAID2759.txt",
    "TG",
)

tn = load_ecad_temperature(
    "data/raw/TN_STAID2759.txt",
    "TN",
)

tx = load_ecad_temperature(
    "data/raw/TX_STAID2759.txt",
    "TX",
)


dataset = (
    tg[["DATE", "TG"]]
    .merge(
        tn[["DATE", "TN"]],
        on="DATE",
    )
    .merge(
        tx[["DATE", "TX"]],
        on="DATE",
    )
)

dataset = dataset.dropna(subset=["DATE", "TG", "TN", "TX"]).copy()

print(dataset.head(10))
print()
print(dataset.shape)

print("\nMissing values:")
print(dataset.isna().sum())

print("\nDuplicate dates:")
print(dataset["DATE"].duplicated().sum())

print("\nDate range:")
print(dataset["DATE"].min())
print(dataset["DATE"].max())

from pathlib import Path

output_path = Path("data/processed/berlin_temperature.csv")

dataset = dataset.sort_values("DATE").reset_index(drop=True)

dataset.to_csv(output_path, index=False)

print(f"\nSaved processed dataset to: {output_path}")
