from pathlib import Path

import pandas as pd


def load_ecad_temperature(
    file_path: str | Path,
    variable: str,
) -> pd.DataFrame:
    """Load an ECA&D temperature series."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    dataset = pd.read_csv(
        path,
        skiprows=21,
        names=[
            "STAID",
            "SOUID",
            "DATE",
            variable,
            f"Q_{variable}",
        ],
        header=None,
    )

    # Remove the repeated CSV header row.
    dataset = dataset[dataset["STAID"] != "STAID"].copy()

    dataset["DATE"] = pd.to_datetime(
        dataset["DATE"],
        format="%Y%m%d",
        errors="coerce",
    )

    # Convert temperature values to numeric.
    dataset[variable] = pd.to_numeric(
        dataset[variable],
        errors="coerce",
    )

    # ECA&D temperature is stored in 0.1 °C.
    dataset[variable] = dataset[variable] / 10

    return dataset
