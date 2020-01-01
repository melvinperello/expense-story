from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, Length, Regexp, EqualTo
from melvinperello_expense_story.controllers import RegisterController


class LoginForm(FlaskForm):
    """Login Form.

    WTF Login Form.

    Attributes:
        username: username data.
        password: password data.
        remember: remember the user upon login.
        submit: submit action.
    """
    username = StringField('Username',validators=[ DataRequired(), Length(min=3, max=30), Regexp("^[a-z]+$",message="Must contain lower case letters only.") ] )
    password = PasswordField('Password', validators=[ DataRequired() , Length(min=8, max=30) , Regexp("^[a-zA-Z0-9]+$",message="Must contain letters or numbers" ) ])
    remember = BooleanField('Remember Me !')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    """Register Form

    WTF Register Form.

    Attributes:
        username: username data.
        password: password data.
        submit: submit action.
    """
    username = StringField('Username',validators=[ DataRequired(), Length(min=3, max=30), Regexp("^[a-z]+$",message="Must contain lower case letters only.") ] )
    password = PasswordField('Password', validators=[ DataRequired() , Length(min=8, max=30) , Regexp("^[a-zA-Z0-9]+$",message="Must contain letters or numbers" ) ])
    confirm_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password') ])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if RegisterController.isUsernameTaken(username.data):
            raise ValidationError('That username is taken. Please choose a different one.')

class FundsAddForm(FlaskForm):
    description = TextAreaField('Description',validators=[ DataRequired(), Length(min=1, max=255) ] )
    fund_type = SelectField(u'Fund Type',choices=[('GENERAL', 'General'), ('INCOME', 'Income'), ('SAVINGS', 'Savings')] )
    submit = SubmitField('Add')
