from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.climate_measurement import ClimateMeasurement
from app.schemas.climate import (
    ClimateForecastRequest,
    ClimateForecastResponse,
    ClimateMeasurementResponse,
    ClimateSummaryResponse,
)
from app.services.climate_data.analysis import analyze_measurements
from app.services.forecasting.predictor import predict_temperature

router = APIRouter(
    prefix="/climate",
    tags=["climate"],
)


@router.get(
    "/measurements",
    response_model=list[ClimateMeasurementResponse],
    summary="Get climate measurements",
    description=(
        "Retrieve climate measurements, optionally filtered by location and date range."
    ),
)
def get_measurements(
    location: str | None = Query(
        default=None,
        description="Filter measurements by location.",
    ),
    start_date: date | None = Query(
        default=None,
        description="Return measurements from this date onward.",
    ),
    end_date: date | None = Query(
        default=None,
        description="Return measurements up to this date.",
    ),
    db: Session = Depends(get_db),
) -> list[ClimateMeasurement]:
    query = db.query(ClimateMeasurement)

    if location:
        query = query.filter(ClimateMeasurement.location == location)

    if start_date:
        query = query.filter(ClimateMeasurement.date >= start_date)

    if end_date:
        query = query.filter(ClimateMeasurement.date <= end_date)

    return query.all()


@router.get(
    "/summary",
    response_model=ClimateSummaryResponse,
    summary="Get climate summary",
    description="Calculate temperature statistics for climate measurements.",
)
def get_summary(
    location: str | None = Query(
        default=None,
        description="Calculate the summary for this location.",
    ),
    db: Session = Depends(get_db),
) -> ClimateSummaryResponse:
    result = analyze_measurements(
        db,
        location=location,
    )

    return ClimateSummaryResponse(
        location=location,
        measurement_count=result["count"],
        average_temperature_c=result["average"],
        minimum_temperature_c=result["minimum"],
        maximum_temperature_c=result["maximum"],
    )


@router.post(
    "/forecast",
    response_model=ClimateForecastResponse,
)
def forecast_temperature(
    request: ClimateForecastRequest,
) -> ClimateForecastResponse:
    features = request.model_dump(
        exclude={"forecast_date"},
    )

    prediction = predict_temperature(features)

    return ClimateForecastResponse(
        location="Berlin-Tempelhof",
        forecast_date=request.forecast_date,
        predicted_temperature_c=prediction,
    )
