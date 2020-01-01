from melvinperello_expense_story import db , bcrypt , app
from melvinperello_expense_story.models import User
from flask_login import login_user

class LoginController():

    def __init__(self):
        self.username = ''
        self.password = ''
        self.remember = False

    def authenticate(self):
        try:
            user = User.query.filter_by(username=self.username).first()
            if user and bcrypt.check_password_hash(user.password, self.password):
                login_user(user, remember=self.remember)
                return True
            else:
                return False
        except Exception as e:
            app.logger.error(str(e))
            return False
        else:
            return False

class RegisterController():
    def __init__(self):
        self.username = ''
        self.password = ''

    def register(self):
        hashed_password = bcrypt.generate_password_hash(self.password).decode('utf-8')
        user = User(username=self.username, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            app.logger.error(str(e))
            return False
        else:
            return True


    @staticmethod
    def isUsernameTaken(username):
        try:
            if User.query.filter_by(username=username).first():
                return True
        except Exception as e:
            app.logger.error(str(e))
            return False
        else:
            return False
