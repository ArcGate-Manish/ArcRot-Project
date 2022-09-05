from flask import session, request, jsonify
from flask_login import login_required
from flask_security.utils import verify_password
from . import login_blueprint
from .. import User
from flask_cors import cross_origin
from sqlalchemy.orm import lazyload

# -------------LOGIN API--------------


@login_blueprint.route('/loginapi', methods=['POST'])
@cross_origin(supports_credentials=True)
def loginapi():
    # print("inside func")
    try:
        _username = request.form['email']
        _password = request.form['password']

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
        return {}


@login_blueprint.route('/logoutapi')
@login_required
def logoutapi():
    if 'email' in session:
        session.pop('username', None)
    # del request.session['email']
    return jsonify({'message': 'You successfully logged out'})
