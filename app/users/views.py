from flask import jsonify
from . import user_blueprint
from .models import User


@user_blueprint.route('/<int:id>/', methods=['GET'])
def get_user_details(id):
    user_details = User.getUserById(id)
    details_list = []
    if (user_details):
        details_list.append({})
        details_list[-1]['user_id'] = user_details.id
        details_list[-1]['first_name'] = user_details.first_name
        details_list[-1]['last_name'] = user_details.last_name
        details_list[-1]['city'] = user_details.city
        details_list[-1]['contact_number'] = user_details.contact_number
        details_list[-1]['email'] = user_details.email
        return jsonify(details_list)
    else:
        return jsonify([])


@user_blueprint.route('/list/', methods=['GET'])
def get_all_user_details():
    user_details = User.getAllUser()
    print(user_details)
    details_list = []
    if (user_details):
        for row in user_details:
            details_list.append({})
            details_list[-1]['user_id'] = row.id
            details_list[-1]['first_name'] = row.first_name
            details_list[-1]['last_name'] = row.last_name
            details_list[-1]['city'] = row.city
            details_list[-1]['contact_number'] = row.contact_number
            details_list[-1]['email'] = row.email
        return jsonify(details_list)
    else:
        return jsonify([])
