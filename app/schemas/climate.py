from datetime import date

from pydantic import BaseModel


class ClimateMeasurementResponse(BaseModel):
    id: int
    date: date
    location: str
    latitude: float
    longitude: float
    temperature_c: float

    model_config = {
        "from_attributes": True,
    }


class ClimateSummaryResponse(BaseModel):
    location: str | None
    measurement_count: int
    average_temperature_c: float | None
    minimum_temperature_c: float | None
    maximum_temperature_c: float | None
