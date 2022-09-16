import email
from lib2to3.pgen2 import token
from flask import session, request, jsonify, make_response
from flask_login import login_required
from flask_security.utils import verify_password
from ..send_mail import confirrm_token, forgot_password_mail
from flask_security.utils import hash_password
from . import login_blueprint
from .. import User
from flask_cors import cross_origin
from sqlalchemy.orm import lazyload


# ##############################################################################
#                                   LOGIN
# ##############################################################################

@login_blueprint.route('/loginapi', methods=['POST'])
@cross_origin(supports_credentials=True)
def loginapi():
    try:

        data = request.get_json()
        _username = data['email']
        _password = data['password']
        if _username and _password:
            result = User.query.options(lazyload(User.roles)).filter(
                User.email == _username).first()
            if result:
                if verify_password(_password, result.password):
                    session['email'] = result.email

                    resp = 1 if result.roles[0].name == 'superuser' else 0
                    return jsonify(resp), 200
                else:
                    resp = jsonify(
                        {'message': 'Bad Request - invalid password'})
                    resp.status_code = 400
                    return resp
            else:
                resp = jsonify(
                    {'message': 'Bad Request - invalid username'})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({'message': 'Bad Request - invalid credendtials'})
            resp.status_code = 400
            return resp
    except Exception as e:
        return "hello"


# ########################################################################################
#                                   LOGOUT
# ########################################################################################

@login_blueprint.route('/logoutapi')
@login_required
def logoutapi():
    if 'email' in session:
        session.pop('username', None)
    # del request.session['email']
    return jsonify({'message': 'You successfully logged out'})


# ########################################################################################
#                                 FORGOT PASSWORD
# ########################################################################################

@login_blueprint.route('/forgotPassword', methods=['POST'])
def forgotPassword():
    if request.json.get('email') is None:
        return make_response(jsonify({'message': "enter a valid email", 'status': 400})), 400
    if not User.query.filter_by(email=request.json.get('email')).first():
        return make_response(jsonify({'message': "No match found! Please enter valid credentials", 'status': 400})), 400
    forgot_password_mail(request.json.get('email'))
    user = User.query.filter(User.email == request.json.get('email')).first()
    user.token_generated = 1
    user.update()
    return make_response(jsonify({'message': 'Email Sent Succesfully.', 'status': 200})), 200


# ########################################################################################
#                                 RESET PASSWORD
# ########################################################################################

@login_blueprint.route('/reset_password', methods=['POST'])
@cross_origin(supports_credentials=True)
def reset_password():
    try: 
        arguments = request.args
        token = arguments.get('token')
        password = request.get_json().get('password')
        confirm_pass = request.get_json().get('confirm_pass')
        confirm_token = confirrm_token(token)
        # print("-----------------",request.__dict__)
        print("++++++++++++++++++++", token,confirm_token, password, confirm_pass)
        if confirm_token:
            user = User.query.filter(User.email == confirm_token).first()
            if user:
                if confirm_token and user.token_generated:

                    if None in [token, confirm_token, password, confirm_pass]:
                        return make_response(jsonify({'message': "Invalid Credentials", 'status': 400})), 400   
                    if password != confirm_pass:
                        return make_response(jsonify({'message': "Passwords dosen't match", 'status': 400})), 400
                    user.password = hash_password(password)
                    user.token_generated = 0
                    user.update()
                    return make_response(jsonify({'message': 'Password reset succesfully.', 'status': 200})), 200

                else:
                    return make_response(jsonify({'message': 'Token Expired.', 'status': 400})), 400
            else:
                return make_response(jsonify({'message': "No match found! Please enter valid credentials", 'status': 400})), 400
            
        else:
            return make_response(jsonify({'message': "Invalid/Expired Token.", 'status': 400})), 400
    except:
        return make_response(jsonify({'message': 'Authentication Error.', 'status': 400})), 400