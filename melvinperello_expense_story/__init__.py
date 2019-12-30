
#
# Please follow Google Style Doc Strings
# https://google.github.io/styleguide/pyguide.html#383-functions-and-methods
#
# ------------------------------------------------------------------------------
# Package Imports
# ------------------------------------------------------------------------------
from flask import Flask




# ------------------------------------------------------------------------------
# Initialize
# ------------------------------------------------------------------------------
app = Flask(__name__)
# configure secret key
app.config['SECRET_KEY'] = 'ace702edd30a3f59c839a4c76a6872e93a36b7616df483600fd22dad61856d2cde3b46458fa024d535a2c6c5bc6f00fd2dca31f14bfc5e7057fcc4b21bee5f10'
db = SQLAlchemy(app)


# ------------------------------------------------------------------------------
# Post-Initialization Imports
# ------------------------------------------------------------------------------
from melvinperello_expense_story import routes
