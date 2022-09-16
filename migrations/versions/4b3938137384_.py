"""empty message

Revision ID: 4b3938137384
Revises: e0465e253649
Create Date: 2022-09-16 12:05:11.658506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b3938137384'
down_revision = 'e0465e253649'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token_generated', sa.SmallInteger(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token_generated')
    # ### end Alembic commands ###
