from flask import Blueprint


post_blueprint = Blueprint('post_blueprint', __name__,
                           template_folder='templates', url_prefix='/post')

from . import views