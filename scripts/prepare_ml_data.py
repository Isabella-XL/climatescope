from pathlib import Path

import pandas as pd

INPUT_PATH = Path("data/processed/berlin_temperature_features.csv")


dataset = pd.read_csv(
    INPUT_PATH,
    parse_dates=["DATE"],
)

dataset = dataset.sort_values("DATE").reset_index(drop=True)


features = [
    "TG_lag_1",
    "TN_lag_1",
    "TX_lag_1",
    "TG_lag_7",
    "TG_rolling_7",
]

target = "TG"


# Use the first 80% for training
# and the final 20% for testing.
split_index = int(len(dataset) * 0.8)

train = dataset.iloc[:split_index].copy()
test = dataset.iloc[split_index:].copy()


X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]


print("Training data:")
print(f"Rows: {len(train)}")
print(f"From: {train['DATE'].min()}")
print(f"To:   {train['DATE'].max()}")

print()

print("Test data:")
print(f"Rows: {len(test)}")
print(f"From: {test['DATE'].min()}")
print(f"To:   {test['DATE'].max()}")

print()

print("Features:")
print(features)

print()

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)
