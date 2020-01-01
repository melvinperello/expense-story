
#
# Please follow Google Style Doc Strings
# https://google.github.io/styleguide/pyguide.html#383-functions-and-methods
#
# ------------------------------------------------------------------------------
# Package Imports
# ------------------------------------------------------------------------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



# ------------------------------------------------------------------------------
# Initialize
# ------------------------------------------------------------------------------
app = Flask(__name__)
# configure secret key
app.config['SECRET_KEY'] = 'ace702edd30a3f59c839a4c76a6872e93a36b7616df483600fd22dad61856d2cde3b46458fa024d535a2c6c5bc6f00fd2dca31f14bfc5e7057fcc4b21bee5f10'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# ------------------------------------------------------------------------------
# Post-Initialization Imports
# ------------------------------------------------------------------------------
from melvinperello_expense_story import routes
