from flask import Blueprint


user_blueprint = Blueprint('user_blueprint', __name__,
                           template_folder='templates', url_prefix='/user')

from . import views