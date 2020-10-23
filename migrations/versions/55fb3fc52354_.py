"""empty message

Revision ID: 55fb3fc52354
Revises: f12e16ae2ef3
Create Date: 2020-10-04 00:20:09.244422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55fb3fc52354'
down_revision = 'f12e16ae2ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('period',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('period_number', sa.Integer(), nullable=True),
    sa.Column('player', sa.Integer(), nullable=True),
    sa.Column('in_stock_product_A', sa.Integer(), nullable=True),
    sa.Column('in_stock_product_B', sa.Integer(), nullable=True),
    sa.Column('in_stock_product_C', sa.Integer(), nullable=True),
    sa.Column('product_A_produced', sa.Integer(), nullable=True),
    sa.Column('product_B_produced', sa.Integer(), nullable=True),
    sa.Column('product_C_produced', sa.Integer(), nullable=True),
    sa.Column('product_A_sold', sa.Integer(), nullable=True),
    sa.Column('product_B_sold', sa.Integer(), nullable=True),
    sa.Column('product_C_sold', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('period')
    # ### end Alembic commands ###
