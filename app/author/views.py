from flask import jsonify, request, make_response
from . import author_blueprint
from .models import Author



# to get details of an author
@author_blueprint.route('/<int:id>/',methods=['GET'])
def get_author_details(id):
    author_details = Author.getAuthorById(id)
    print(author_details)
    details_list ={}
    if(author_details):
        details_list['author_id'] = author_details.id
        details_list['description'] = author_details.description
        return jsonify(details_list)
    else:
        return jsonify([])


"""@author_blueprint.route('/<int:id>/',methods=['POST'])
def update_author(id):
    author = Author.getAuthorById(id)
    result = {}
    if(author):
        data = request.form['description']
        author.description = data
        author.update()
        # status = 200
        result = {
            'status' : 'Success'
        }
    return make_response(result), 200
"""
@author_blueprint.route('/list/',methods=['GET'])
def get_all_author_details():
    author_details = Author.getAllAuthor()
    print(author_details)
    details_list ={}
    if(author_details):
        for row in author_details:
            details_list[row.id] = {}
            details_list[row.id]['author_id'] = row.id
            details_list[row.id]['description'] = row.description
        return jsonify(details_list)
    else:
        return jsonify([])
