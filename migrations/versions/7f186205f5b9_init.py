"""Init

Revision ID: 7f186205f5b9
Revises: 
Create Date: 2023-06-19 10:53:27.210022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f186205f5b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(precision=8, asdecimal=2), nullable=False),
    sa.Column('inventory_quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
