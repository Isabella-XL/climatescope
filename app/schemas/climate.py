from datetime import date

from pydantic import BaseModel


class ClimateMeasurementResponse(BaseModel):
    id: int
    date: date
    location: str
    latitude: float
    longitude: float
    mean_temperature_c: float
    min_temperature_c: float
    max_temperature_c: float

    model_config = {
        "from_attributes": True,
    }


class ClimateSummaryResponse(BaseModel):
    location: str | None
    measurement_count: int
    average_temperature_c: float | None
    minimum_temperature_c: float | None
    maximum_temperature_c: float | None


class ClimateForecastRequest(BaseModel):
    forecast_date: date
    TG_lag_1: float
    TN_lag_1: float
    TX_lag_1: float
    TG_lag_7: float
    TG_rolling_7: float
    TG_rolling_14: float
    day_of_year_sin: float
    day_of_year_cos: float


class ClimateForecastResponse(BaseModel):
    location: str
    forecast_date: date
    predicted_temperature_c: float
