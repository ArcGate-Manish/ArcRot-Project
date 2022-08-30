from flask import jsonify
from . import user_blueprint
from .models import User




@user_blueprint.route('/<int:id>/',methods=['GET'])
def get_user_details(id):
    user_details = User.getUserById(id)
    print(user_details)
    details_list ={}
    if(user_details):
        details_list['user_id'] = user_details.id
        details_list['first_name'] = user_details.first_name
        details_list['last_name'] = user_details.last_name
        details_list['city'] = user_details.city
        details_list['contact_number'] = user_details.contact_number
        details_list['email'] = user_details.email
        return jsonify(details_list)
    else:
        return jsonify([])



@user_blueprint.route('/list/',methods=['GET'])
def get_all_user_details():
    user_details = User.getAllUser()
    print(user_details)
    details_list ={}
    if(user_details):
        for row in user_details:
            details_list[row.id] = {}
            details_list[row.id]['user_id'] = row.id
            details_list[row.id]['first_name'] = row.first_name
            details_list[row.id]['last_name'] = row.last_name
            details_list[row.id]['city'] = row.city
            details_list[row.id]['contact_number'] = row.contact_number
            details_list[row.id]['email'] = row.email
        return jsonify(details_list)
    else:
        return jsonify([])
