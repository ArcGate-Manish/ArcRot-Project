"""empty message

Revision ID: ee942cf5ada0
Revises: 
Create Date: 2022-09-05 12:20:07.902028

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee942cf5ada0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_images', sa.Column('post_image_created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.drop_index('postimg_created_at', table_name='post_images')
    op.create_index(op.f('post_image_created_at'), 'post_images', ['post_image_created_at'], unique=False)
    op.drop_column('post_images', 'postimg_created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_images', sa.Column('postimg_created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False))
    op.drop_index(op.f('post_image_created_at'), table_name='post_images')
    op.create_index('postimg_created_at', 'post_images', ['postimg_created_at'], unique=False)
    op.drop_column('post_images', 'post_image_created_at')
    # ### end Alembic commands ###
