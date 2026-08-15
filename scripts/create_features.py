from pathlib import Path

import numpy as np
import pandas as pd

INPUT_PATH = Path("data/processed/berlin_temperature.csv")
OUTPUT_PATH = Path("data/processed/berlin_temperature_features.csv")


dataset = pd.read_csv(
    INPUT_PATH,
    parse_dates=["DATE"],
)

dataset = dataset.sort_values("DATE").reset_index(drop=True)

dataset["day_of_year"] = dataset["DATE"].dt.dayofyear

dataset["day_of_year_sin"] = np.sin(2 * np.pi * dataset["day_of_year"] / 365.25)

dataset["day_of_year_cos"] = np.cos(2 * np.pi * dataset["day_of_year"] / 365.25)

# Previous day's temperatures
dataset["TG_lag_1"] = dataset["TG"].shift(1)
dataset["TN_lag_1"] = dataset["TN"].shift(1)
dataset["TX_lag_1"] = dataset["TX"].shift(1)

# Temperature from 7 days ago
dataset["TG_lag_7"] = dataset["TG"].shift(7)

# Rolling average of the previous 7 days.
# shift(1) makes sure today's temperature is not included.
dataset["TG_rolling_7"] = dataset["TG"].shift(1).rolling(7).mean()

dataset["TG_rolling_14"] = dataset["TG"].shift(1).rolling(14).mean()

# Remove rows where we don't have enough historical data.
dataset = dataset.dropna().copy()

dataset.to_csv(
    OUTPUT_PATH,
    index=False,
)

print(dataset.head())
print()
print(dataset.columns.tolist())
print()
print(f"Rows: {len(dataset)}")
print(f"Saved to: {OUTPUT_PATH}")
