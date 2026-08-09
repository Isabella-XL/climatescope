from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ClimateDataset(Base):
    __tablename__ = "climate_datasets"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
    source: Mapped[str]
