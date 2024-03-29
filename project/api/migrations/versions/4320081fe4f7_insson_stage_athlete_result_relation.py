"""insson stage athlete result relation

Revision ID: 4320081fe4f7
Revises: e1554b0016fe
Create Date: 2021-09-30 11:09:23.282098

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4320081fe4f7'
down_revision = 'e1554b0016fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('results', 'athlete_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('results', 'stage_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('results', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.alter_column('results', 'stage_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('results', 'athlete_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
