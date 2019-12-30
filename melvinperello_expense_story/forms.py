from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp


class LoginForm(FlaskForm):
    """Login Form.

    WTF Login Form.

    Attributes:
        username: username data.
        password: password data.
        remember: remember the user upon login.
        submit: submit action.
    """
    username = StringField('Username',validators=[ DataRequired(), Length(min=3, max=30), Regexp("[a-z]",message="Must contain lower case letters only.") ] )
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me !')
    submit = SubmitField('Login')
