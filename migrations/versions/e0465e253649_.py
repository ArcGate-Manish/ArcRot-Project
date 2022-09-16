"""empty message

Revision ID: e0465e253649
Revises: 5e5e0d0bb09f
Create Date: 2022-09-16 11:39:17.858397

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e0465e253649'
down_revision = '5e5e0d0bb09f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('created_at', table_name='uploads')
    op.drop_table('uploads')
    # op.add_column('users', sa.Column('token_generated', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_column('users', 'token_generated')
    op.create_table('uploads',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('path', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('width', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mimetype', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('original', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['club_members.id'], name='fk_uploads_profile_id'),
    sa.PrimaryKeyConstraint('id', name='pk_uploads')
    )
    op.create_index('created_at', 'uploads', ['created_at'], unique=False)
    # ### end Alembic commands ###
