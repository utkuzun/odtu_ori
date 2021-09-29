"""club comp relation added

Revision ID: ffb1067151e6
Revises: d93f00fdc2e3
Create Date: 2021-09-28 11:19:49.136077

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ffb1067151e6'
down_revision = 'd93f00fdc2e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('club_comp',
    sa.Column('club_id', sa.Integer(), nullable=True),
    sa.Column('competition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['club_id'], ['clubs.id'], ),
    sa.ForeignKeyConstraint(['competition_id'], ['competitions.id'], )
    )
    op.drop_table('club_stage')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('club_stage',
    sa.Column('club_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stage_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['club_id'], ['clubs.id'], name='club_stage_ibfk_1'),
    sa.ForeignKeyConstraint(['stage_id'], ['stages.id'], name='club_stage_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('club_comp')
    # ### end Alembic commands ###
