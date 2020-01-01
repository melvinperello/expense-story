from melvinperello_expense_story import db , bcrypt , app
from melvinperello_expense_story.models import User , Fund
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

class FundController():
    def __init__(self):
        self.description = ''
        self.fund_type = ''
        self.user_id = None

    def insert(self):
        fund = Fund(description=self.description, fund_type=self.fund_type, user_id=self.user_id)
        try:
            db.session.add(fund)
            db.session.commit()
        except Exception as e:
            app.logger.error(str(e))
            return False
        else:
            return True

    @staticmethod
    def getAll(user_id):
        try:
            funds = Fund.query.filter_by(user_id=user_id).all()
            return funds
        except Exception as e:
            app.logger.error(str(e))
            return False
        else:
            return False
