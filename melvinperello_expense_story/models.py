from melvinperello_expense_story import db

class User(db.Model):
    """User Model

    Object Representation of the User table.

    Attributes:
        id: unique auto generated id.
        username: unique identifiable username for logging in.
        password: hashed password.
        state: user account status
            [CREATED] the user was registered but is not allowed to logged in.
            [VERIFIED] the user was verified by an admin user.
        role: access level of the user.
            [USER] a normal user.
            [ADMIN] can verify a created user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(20), nullable=False, default='CREATED')
    role = db.Column(db.String(20), nullable=False, default='USER')
