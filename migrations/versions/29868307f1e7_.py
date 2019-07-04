"""empty message

Revision ID: 29868307f1e7
Revises: 05034a90809d
Create Date: 2019-06-05 19:08:03.071026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29868307f1e7'
down_revision = '05034a90809d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('board')
    # ### end Alembic commands ###