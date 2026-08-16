"""add min max mean temperatures

Revision ID: a3370795c499
Revises: 1e70b0bbdacb
Create Date: 2026-08-16 12:58:57.738352

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a3370795c499"
down_revision: Union[str, Sequence[str], None] = "1e70b0bbdacb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.alter_column(
        "climate_measurements",
        "temperature_c",
        new_column_name="mean_temperature_c",
    )

    op.add_column(
        "climate_measurements",
        sa.Column(
            "min_temperature_c",
            sa.Float(),
            nullable=True,
        ),
    )

    op.add_column(
        "climate_measurements",
        sa.Column(
            "max_temperature_c",
            sa.Float(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "climate_measurements",
        "max_temperature_c",
    )

    op.drop_column(
        "climate_measurements",
        "min_temperature_c",
    )

    op.alter_column(
        "climate_measurements",
        "mean_temperature_c",
        new_column_name="temperature_c",
    )
    # ### end Alembic commands ###
