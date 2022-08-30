from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import input_required


class loginForm(FlaskForm):
    username = StringField('USERNAME', validators=[input_required(message='A username is required!')])
    password = PasswordField('PASSWORD', validators=[input_required(message='password is required!')])
    submit = SubmitField('Submit')