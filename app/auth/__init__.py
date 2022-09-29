from flask import Blueprint


login_blueprint = Blueprint(
    'login_blueprint', __name__, template_folder='templates')

from . import view