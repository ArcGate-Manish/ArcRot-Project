import os
from os.path import join, dirname, abspath
from flask import (Flask, render_template, 
                    send_from_directory, make_response, abort)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
from flask_login import login_required
from flask_wtf.csrf import CSRFProtect

basedir = abspath(dirname(__file__))
infofilename = join(basedir)
filename = join(basedir)


app = Flask(__name__, instance_relative_config=True)
CORS(app, supports_credentials= True)
mail = Mail(app)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config.from_object('config.default')
app.config.from_object('config.development')
# app.config.from_object('config.production')
app.config.from_object('config.admin_config')
app.config.from_pyfile('config.py')


convention = {
    "ix": '%(column_0_name)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


basedir = abspath(dirname(__file__))
uploads_dir = join(basedir, 'uploads')
app.config['BASE_DIR'] = basedir
app.config['UPLOADS_DIR'] = uploads_dir
app.config['POSTS_IMAGES_UPLOADS_DIR'] = join(uploads_dir, 'post_images/')
app.config['PROFILE_IMAGES_UPLOADS_DIR'] = join(uploads_dir, 'profile_images/')

 
from .users.models import Role, User
from .author.models import Author
from .clubs.models import Club, ClubMembers
from .posts.models import Post, PostImages, Tag
from .events.models import Event
from .uploads.model import Uploads


from .admin import admin_blueprint
from .author import author_blueprint
from .users import user_blueprint
from .clubs import club_blueprint
from .posts import post_blueprint
from .auth import login_blueprint
from .events import event_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(club_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(author_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(event_blueprint)


csrf.exempt(login_blueprint)


# Setup commands
from .admin.commands import create_database
app.cli.add_command(create_database)



@app.route('/')
def index():
    return render_template('index.html')

