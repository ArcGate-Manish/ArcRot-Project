"""empty message

Revision ID: 088702e25241
Revises: 91870711ec7a
Create Date: 2022-09-14 10:43:18.980780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '088702e25241'
down_revision = '91870711ec7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_club_members_club_member_email'), 'club_members', ['club_member_email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_club_members_club_member_email'), 'club_members', type_='unique')
    # ### end Alembic commands ###
