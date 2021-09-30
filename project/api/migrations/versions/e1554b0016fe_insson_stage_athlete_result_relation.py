"""insson stage athlete result relation

Revision ID: e1554b0016fe
Revises: 1de468a5505e
Create Date: 2021-09-30 11:04:33.545786

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e1554b0016fe'
down_revision = '1de468a5505e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('results', 'athlete_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('results', 'stage_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('results', 'stage_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('results', 'athlete_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('results', 'id')
    # ### end Alembic commands ###
