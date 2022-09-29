from flask import Blueprint


club_blueprint = Blueprint('club_blueprint', __name__,
                           template_folder='templates', url_prefix='/club')

from . import views