from melvinperello_expense_story import db , bcrypt
from melvinperello_expense_story.models import User

class LoginController():

    def __init__(self):
        self.username = ''
        self.password = ''

    def authenticate(self):
        if self.username == 'melvinperello' and self.password == '123456':
            return True
        else:
            return False

class RegisterController():
    def __init__(self):
        self.username = ''
        self.password = ''

    def register(self):
        hashed_password = bcrypt.generate_password_hash(self.password).decode('utf-8')
        user = User(username=self.username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        pass
