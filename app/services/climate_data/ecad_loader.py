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


def load_ecad_temperature_dataset(
    tg_path: str | Path,
    tn_path: str | Path,
    tx_path: str | Path,
) -> pd.DataFrame:
    """Load and combine ECA&D TG, TN, and TX temperature series."""

    tg = load_ecad_temperature(tg_path, "TG")
    tn = load_ecad_temperature(tn_path, "TN")
    tx = load_ecad_temperature(tx_path, "TX")

    dataset = tg[["DATE", "TG"]].merge(
        tn[["DATE", "TN"]],
        on="DATE",
        how="inner",
    )

    dataset = dataset.merge(
        tx[["DATE", "TX"]],
        on="DATE",
        how="inner",
    )

    dataset = dataset.dropna(subset=["DATE", "TG", "TN", "TX"]).copy()

    dataset = dataset.sort_values("DATE").reset_index(drop=True)

    return dataset
