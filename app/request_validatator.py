# from functools import wraps
# from flask import request, make_response, jsonify, abort
# from flask_security import current_user
# from app. users.models import roles_users
# from app.users.models import User






# def get_request_field_empty_validation(fields):
#     """Make sure GET request have require fields not empty before proceeding"""
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for field in fields:
#                 if request.values.get(field) == "":
#                     return make_response(jsonify(subcode=4002, message="{f} field can not empty".format(f=field), field=field)), 400
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


# def requires_access_level(func):
#     @wraps(func)
#     def decorated_function(*args, **kwargs):
#         if current_user and not current_user.isAdmin():
#             result =  roles_users.getAllActive()
#             permission = {}
#             all_route = []
#             for row in result:
#                 permission[row.id] = row.route
            
#                 all_route.append(row.route)
#             role_permissions  = User.getAllByRoleId(current_user,id)
              
#             user_allowed = []
#             for row in role_permissions:
#                 if permission.__contains__(row.permission_routes_id):
#                     user_allowed.append(permission[row.permission_routes_id])

            
#             endpoint = request.endpoint
#             if endpoint in all_route:
#                 if not request.endpoint in user_allowed:
#                     abort(403)
#         return func(*args, **kwargs)
#     return decorated_function