from flask import Blueprint


event_blueprint = Blueprint(
    'event_blueprint', __name__, template_folder='templates', url_prefix='/event')

from . import views