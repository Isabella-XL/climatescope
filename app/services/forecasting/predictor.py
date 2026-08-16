from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path("data/processed/berlin_temperature_model.joblib")

FEATURES = [
    "TG_lag_1",
    "TN_lag_1",
    "TX_lag_1",
    "TG_lag_7",
    "TG_rolling_7",
    "TG_rolling_14",
    "day_of_year_sin",
    "day_of_year_cos",
]


def load_model():
    """Load the trained Berlin temperature model."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    return joblib.load(MODEL_PATH)


def predict_temperature(features: dict[str, float]) -> float:
    """Predict mean temperature using the trained model."""
    model = load_model()

    input_data = pd.DataFrame(
        [[features[name] for name in FEATURES]],
        columns=FEATURES,
    )

    prediction = model.predict(input_data)[0]

    return float(prediction)
