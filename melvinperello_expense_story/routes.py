from flask import render_template
from melvinperello_expense_story import app



@app.route("/" , methods=['GET'])
def home():
    """Display the home page.

    [GET]   This will display the main view of the application.

    Args:

    Returns:
        HTML

    Raises:

    """
    return "home"


@app.route("/login" , methods=['GET','POST'])
def login():
    """Display the login page.

    [GET]   Display the login page form.
    [POST]  Action handler to the login form.

    Args:


    Returns:
        HTML

    Raises:

    """
    return "login"

@app.route("/register" , methods=['GET','POST'])
def register():
    """Display the registration page.

    [GET]   Display the registration page form.
    [POST]  Action handler to the registration form.

    Args:


    Returns:
        HTML

    Raises:

    """
    return "register"

@app.route("/accounts" , methods=['GET','POST'])
def accounts():
    """Display the registration page.

    [GET]   Display the registration page form.
    [POST]  Action handler to the registration form.

    Args:


    Returns:
        HTML

    Raises:

    """
    return "accounts"

@app.route("/accounts/<int:id>" , methods=['GET','PUT','DELETE'])
def account(id):
    return "account"
