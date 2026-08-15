from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

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
    "TG_rolling_14",
    "day_of_year_sin",
    "day_of_year_cos",
]

target = "TG"


# Time-based train/test split
split_index = int(len(dataset) * 0.8)

train = dataset.iloc[:split_index].copy()
test = dataset.iloc[split_index:].copy()


X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]


# Create the model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
)


# Train the model
model.fit(X_train, y_train)

MODEL_PATH = Path("data/processed/berlin_temperature_model.joblib")

joblib.dump(model, MODEL_PATH)

print(f"Model saved to: {MODEL_PATH}")


# Make predictions
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)

baseline_predictions = test["TG_lag_1"]

baseline_mae = mean_absolute_error(
    y_test,
    baseline_predictions,
)

baseline_rmse = root_mean_squared_error(
    y_test,
    baseline_predictions,
)

improvement = (baseline_mae - mae) / baseline_mae * 100

print()
print(f"MAE improvement: {improvement:.1f}%")

print()
print("Baseline:")
print(f"MAE:  {baseline_mae:.2f} °C")
print(f"RMSE: {baseline_rmse:.2f} °C")


print()
print(f"MAE:  {mae:.2f} °C")
print(f"RMSE: {rmse:.2f} °C")


print("Model trained successfully.")
print()
print("Predictions:")
print(predictions[:10])
print()
print("Actual values:")
print(y_test.head(10).to_numpy())
