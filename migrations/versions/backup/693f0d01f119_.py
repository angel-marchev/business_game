"""empty message

Revision ID: 693f0d01f119
Revises: 11e4be584da8
Create Date: 2020-11-01 20:34:04.806428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693f0d01f119'
down_revision = '11e4be584da8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('period', sa.Column('products_in_stock_beginning_of_period', sa.Integer(), nullable=True))
    op.drop_column('period', 'products_in_stock_beggining_of_period')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('period', sa.Column('products_in_stock_beggining_of_period', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('period', 'products_in_stock_beginning_of_period')
    # ### end Alembic commands ###
