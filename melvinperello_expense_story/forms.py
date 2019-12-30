from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Login Form.

    WTF Login Form.

    Attributes:
        username: username data.
        password: password data.
        remember: remember the user upon login.
        submit: submit action.
    """
    username = StringField('Username',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me !')
    submit = SubmitField('Login')
