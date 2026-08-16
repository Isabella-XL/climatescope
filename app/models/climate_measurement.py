from datetime import date as date_type

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ClimateMeasurement(Base):
    __tablename__ = "climate_measurements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[date_type] = mapped_column(Date, nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    mean_temperature_c: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    min_temperature_c: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    max_temperature_c: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )
