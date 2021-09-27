"""update club

Revision ID: 475910fe92e5
Revises: 7dd85f48b187
Create Date: 2021-09-06 11:18:27.969154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '475910fe92e5'
down_revision = '7dd85f48b187'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clubs', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clubs', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
