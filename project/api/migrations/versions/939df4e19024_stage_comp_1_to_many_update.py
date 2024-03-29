"""stage comp 1 to many update

Revision ID: 939df4e19024
Revises: 10ee3e1bb422
Create Date: 2021-09-24 11:17:20.747128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '939df4e19024'
down_revision = '10ee3e1bb422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stage_comp')
    op.add_column('stages', sa.Column('competition_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stages', 'competitions', ['competition_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stages', type_='foreignkey')
    op.drop_column('stages', 'competition_id')
    op.create_table('stage_comp',
    sa.Column('stage_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('competition_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['competition_id'], ['competitions.id'], name='stage_comp_ibfk_1'),
    sa.ForeignKeyConstraint(['stage_id'], ['stages.id'], name='stage_comp_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
