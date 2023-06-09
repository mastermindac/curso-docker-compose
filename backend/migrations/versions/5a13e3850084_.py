"""empty message

Revision ID: 5a13e3850084
Revises: 68d55b0b30e6
Create Date: 2023-04-25 17:34:17.245841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a13e3850084'
down_revision = '68d55b0b30e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('date', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'date')
    # ### end Alembic commands ###
