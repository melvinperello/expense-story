class LoginController():

    def __init__(self):
        self.username = ''
        self.password = ''

    def authenticate(self):
        if self.username == 'melvinperello' and self.password == '123456':
            return True
        else:
            return False
