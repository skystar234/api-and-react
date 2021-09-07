"""empty message

Revision ID: 9901a34e92df
Revises: 59f561a7d947
Create Date: 2021-09-05 23:42:42.742302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9901a34e92df'
down_revision = '59f561a7d947'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction', '_value')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('_value', sa.INTEGER(), nullable=False))
    # ### end Alembic commands ###
