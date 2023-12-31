"""reviewss  table

Revision ID: 44312189fa1d
Revises: 3ec7cf2055fd
Create Date: 2023-09-04 14:50:50.614055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44312189fa1d'
down_revision: Union[str, None] = '3ec7cf2055fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('star_rating', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Reviews')
    op.drop_table('Restaurants')
    op.drop_table('Customers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Restaurants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Reviews',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('comment', sa.VARCHAR(), nullable=True),
    sa.Column('star_rating', sa.INTEGER(), nullable=True),
    sa.Column('restaurant_id', sa.INTEGER(), nullable=True),
    sa.Column('customer_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reviews')
    op.drop_table('restaurants')
    op.drop_table('customers')
    # ### end Alembic commands ###
