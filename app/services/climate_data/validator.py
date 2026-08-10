import pandas as pd

REQUIRED_COLUMNS = {
    "date",
    "location",
    "latitude",
    "longitude",
    "temperature_c",
}


def validate_columns(dataset: pd.DataFrame) -> None:
    """Validate that all required climate columns exist."""
    missing = REQUIRED_COLUMNS - set(dataset.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
