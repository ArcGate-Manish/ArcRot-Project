from flask import Flask, url_for, render_template,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
import flask_admin
from flask_admin import helpers as admin_helpers
from .. import db, app
from .. import Role, ClubMembers, Club, Tag, Author, Post, PostImages, User


admin_blueprint = Blueprint('admin_blueprint', __name__,template_folder='templates')


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create admin
admin = flask_admin.Admin(
    app,
    'My Dashboard',
    base_template='my_master.html',
    template_mode='bootstrap4',
)
# Add model views

from .views import MyModelView
admin.add_view(MyModelView(Role, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Roles"))
admin.add_view(MyModelView(Club, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Clubs"))
admin.add_view(MyModelView(ClubMembers, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Club Members"))
admin.add_view(MyModelView(Tag, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Tags"))
admin.add_view(MyModelView(Author, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Author"))
admin.add_view(MyModelView(Post, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Posts"))
admin.add_view(MyModelView(PostImages, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Post Images"))
admin.add_view(MyModelView(User, db.session, menu_icon_type='fa', menu_icon_value='fa-users', name="Users"))
# admin.add_view(CustomView(name="Custom view", endpoint='custom', menu_icon_type='fa', menu_icon_value='fa-connectdevelop',))

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )

