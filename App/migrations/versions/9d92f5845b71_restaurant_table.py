"""restaurant table

Revision ID: 9d92f5845b71
Revises: b0906533b423
Create Date: 2023-09-04 14:35:05.735168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d92f5845b71'
down_revision: Union[str, None] = 'b0906533b423'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Reviews', sa.Column('star_rating', sa.Integer(), nullable=True))
    op.add_column('Reviews', sa.Column('restaurant_id', sa.Integer(), nullable=True, Foreign_Key=True))
    op.add_column('Reviews', sa.Column('customer_id', sa.Integer(), nullable=True, Foreign_Ke=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Reviews', 'customer_id')
    op.drop_column('Reviews', 'restaurant_id')
    op.drop_column('Reviews', 'star_rating')
    # ### end Alembic commands ###
