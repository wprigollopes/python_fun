"""seed cities data

Revision ID: 2cf1f42bb4f6
Revises: 172a13028191
Create Date: 2026-03-20 09:14:08.263637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cf1f42bb4f6'
down_revision: Union[str, Sequence[str], None] = '172a13028191'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    cities_table = sa.table(
        "cities",
        sa.column("name", sa.String),
        sa.column("state", sa.String),
        sa.column("population", sa.Integer),
    )

    op.bulk_insert(cities_table, [
        {"name": "São Paulo", "state": "SP", "population": 12_325_232},
        {"name": "Rio de Janeiro", "state": "RJ", "population": 6_747_815},
        {"name": "Brasília", "state": "DF", "population": 3_094_325},
        {"name": "Salvador", "state": "BA", "population": 2_886_698},
        {"name": "Fortaleza", "state": "CE", "population": 2_703_391},
        {"name": "Belo Horizonte", "state": "MG", "population": 2_530_701},
        {"name": "Manaus", "state": "AM", "population": 2_255_903},
        {"name": "Curitiba", "state": "PR", "population": 1_963_726},
        {"name": "Recife", "state": "PE", "population": 1_661_681},
        {"name": "Porto Alegre", "state": "RS", "population": 1_492_530},
    ])


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM cities")
