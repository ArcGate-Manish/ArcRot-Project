from flask import Blueprint


author_blueprint = Blueprint(
    'author_blueprint', __name__, template_folder='templates', url_prefix='/author')
from . import views