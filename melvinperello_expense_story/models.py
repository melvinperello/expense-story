from melvinperello_expense_story import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    """Call back for the Flask Login extension

    allows the  flask login to get user session details.

    Args:
        user_id (int): user id.

    Returns:
        User

    Raises:

    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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

    def __repr__(self):
        return f"model.User: {vars(self)}"


class Fund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    fund_type = db.Column(db.String(50), nullable=False, default='GENERAL')

    def __repr__(self):
        return f"model.Fund: {vars(self)}"
