"""empty message

Revision ID: 4e214f6d3925
Revises: 
Create Date: 2023-12-25 18:37:38.603611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e214f6d3925'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('level', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('exp', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'exp')
    op.drop_column('users', 'level')
    # ### end Alembic commands ###
