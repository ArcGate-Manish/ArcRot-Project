from flask import jsonify, request, make_response
from . import author_blueprint
from .models import Author


# to get details of an author
@author_blueprint.route('/<int:id>/', methods=['GET'])
def get_author_details(id):
    author_details = Author.getAuthorById(id)
    details_list = []
    if (author_details):
        details_list.append({})
        details_list[-1]['author_id'] = author_details.id
        details_list[-1]['description'] = author_details.description
        return jsonify(details_list)
    else:
        return jsonify([])


@author_blueprint.route('/list/', methods=['GET'])
def get_all_author_details():
    author_details = Author.getAllAuthor()
    details_list = []
    if (author_details):
        for row in author_details:
            details_list.append({})
            details_list[-1]['author_id'] = row.id
            details_list[-1]['description'] = row.description
        return jsonify(details_list)
    else:
        return jsonify([])
