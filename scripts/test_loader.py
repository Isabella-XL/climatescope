from app.services.climate_data.loader import load_csv
from app.services.climate_data.validator import validate_columns

dataset = load_csv("data/raw/climate_sample.csv")

validate_columns(dataset)

print("Dataset validation successful.")
print(dataset)
