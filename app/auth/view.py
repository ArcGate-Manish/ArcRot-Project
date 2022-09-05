import imp
from flask import flash, render_template, session, redirect, url_for, request, jsonify,make_response
from flask_login import login_required, login_manager, logout_user, login_user
from flask_security.utils import verify_password
from . import login_blueprint
from .. import User, db
from .form import loginForm
from sqlalchemy import text
from flask_cors import cross_origin


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if (request.method == 'POST'):
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.username.data).first()
            if user and verify_password(form.password.data, user.password):
                session['email'] = user.email
                login_user(user)
                # flash('login successful')
                return render_template('home.html')
    return render_template('login.html', form=form)


@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('login_blueprint.login'))


@login_blueprint.route('/home')
def home():
    if 'email' in session:
        username = session['email']
        return jsonify({'message': 'You are already logged in', 'username': username})
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp

# -------------LOGIN API--------------

@login_blueprint.route('/loginapi', methods=['POST'])
@cross_origin(supports_credentials=True)
def loginapi():
    # print("inside func")
    try:
        _username = request.form['email']
        _password = request.form['password']

        if _username and _password:
            result = User.query.filter(User.email == _username).first()
            # print(result)
            if result:
                if verify_password(_password, result.password):
                    session['email'] = result.email
                    resp = jsonify({'message': 'You are logged in successfully'})
                    # resp.headers.add("Access-Control-Allow-Origin", "*")
                    return resp, 200
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
        # print("inside except")
        return "inside except"


@login_blueprint.route('/logoutapi')
@login_required
def logoutapi():
    if 'email' in session:
        session.pop('username', None)
    # del request.session['email']
    return jsonify({'message': 'You successfully logged out'})
