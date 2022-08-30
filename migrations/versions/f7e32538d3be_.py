"""empty message

Revision ID: f7e32538d3be
Revises: 
Create Date: 2022-08-10 12:20:08.000835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7e32538d3be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clubs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('email_id', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_clubs')),
    sa.UniqueConstraint('email_id', name=op.f('uq_clubs_email_id')),
    sa.UniqueConstraint('name', name=op.f('uq_clubs_name'))
    )
    op.create_index(op.f('created_at'), 'clubs', ['created_at'], unique=False)
    op.create_index(op.f('is_active'), 'clubs', ['is_active'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles'))
    )
    op.create_index(op.f('created_at'), 'roles', ['created_at'], unique=False)
    op.create_index(op.f('name'), 'roles', ['name'], unique=False)
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tags')),
    sa.UniqueConstraint('name', name=op.f('uq_tags_name'))
    )
    op.create_index(op.f('created_at'), 'tags', ['created_at'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('image_name', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('contact_number', sa.BigInteger(), nullable=True),
    sa.Column('email_id', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.SmallInteger(), nullable=False),
    sa.Column('is_admin', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email_id', name=op.f('uq_users_email_id')),
    sa.UniqueConstraint('image_name', name=op.f('uq_users_image_name'))
    )
    op.create_index(op.f('created_at'), 'users', ['created_at'], unique=False)
    op.create_index(op.f('is_active'), 'users', ['is_active'], unique=False)
    op.create_index(op.f('is_admin'), 'users', ['is_admin'], unique=False)
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_author_user_id')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_author'))
    )
    op.create_index(op.f('user_id'), 'author', ['user_id'], unique=True)
    op.create_table('club_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('club_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('member_from', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('member_till', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_active', sa.SmallInteger(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['club_id'], ['clubs.id'], name=op.f('fk_club_members_club_id')),
    sa.ForeignKeyConstraint(['member_id'], ['users.id'], name=op.f('fk_club_members_member_id')),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_club_members_role_id')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_club_members'))
    )
    op.create_index(op.f('is_active'), 'club_members', ['is_active'], unique=False)
    op.create_index(op.f('member_from'), 'club_members', ['member_from'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('cover_image_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name=op.f('fk_posts_author_id')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_posts'))
    )
    op.create_index(op.f('author_id'), 'posts', ['author_id'], unique=False)
    op.create_index(op.f('created_at'), 'posts', ['created_at'], unique=False)
    op.create_table('post_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name=op.f('fk_post_images_post_id')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_post_images'))
    )
    op.create_index(op.f('created_at'), 'post_images', ['created_at'], unique=False)
    op.create_index(op.f('post_id'), 'post_images', ['post_id'], unique=False)
    op.create_table('post_tag',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name=op.f('fk_post_tag_post_id')),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name=op.f('fk_post_tag_tag_id')),
    sa.PrimaryKeyConstraint('post_id', 'tag_id', name=op.f('pk_post_tag'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tag')
    op.drop_index(op.f('post_id'), table_name='post_images')
    op.drop_index(op.f('created_at'), table_name='post_images')
    op.drop_table('post_images')
    op.drop_index(op.f('created_at'), table_name='posts')
    op.drop_index(op.f('author_id'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('member_from'), table_name='club_members')
    op.drop_index(op.f('is_active'), table_name='club_members')
    op.drop_table('club_members')
    op.drop_index(op.f('user_id'), table_name='author')
    op.drop_table('author')
    op.drop_index(op.f('is_admin'), table_name='users')
    op.drop_index(op.f('is_active'), table_name='users')
    op.drop_index(op.f('created_at'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('created_at'), table_name='tags')
    op.drop_table('tags')
    op.drop_index(op.f('name'), table_name='roles')
    op.drop_index(op.f('created_at'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('is_active'), table_name='clubs')
    op.drop_index(op.f('created_at'), table_name='clubs')
    op.drop_table('clubs')
    # ### end Alembic commands ###
