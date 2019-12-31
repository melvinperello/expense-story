from flask import render_template, url_for, flash, redirect
from melvinperello_expense_story import app
from melvinperello_expense_story.forms import LoginForm , RegisterForm
from melvinperello_expense_story.controllers import LoginController , RegisterController

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
    form = LoginForm()
    if form.validate_on_submit():
        # form is valid
        # proceed authentication
        controller = LoginController()
        controller.username = form.username.data
        controller.password = form.password.data

        if controller.authenticate():
            return redirect(url_for('accounts'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', form=form)

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
    form = RegisterForm()
    if form.validate_on_submit():
        controller = RegisterController()
        controller.username = form.username.data
        controller.password = form.password.data
        controller.register()
    return render_template('register.html', form=form)

@app.route("/accounts" , methods=['GET','POST'])
def accounts():
    """Display all accounts owned by the user.

    [GET]   Display all accounts for the user.
    [POST]  Add account to the user.

    Args:


    Returns:
        HTML

    Raises:

    """
    return "accounts"

@app.route("/accounts/<int:account_id>" , methods=['GET','PUT','DELETE'])
def account(account_id):
    """Display a specific account owned by the user.

    [GET]   Display the account using the account id.
    [PUT]   Update the account using the account id.
    [DELETE] Delete the account using the account id.

    Args:
        account_id (int): the account id.

    Returns:
        HTML

    Raises:

    """
    return "account"

@app.route("/transactions/accounts/<int:account_id>" , methods=['GET','POST'])
def transactions(account_id):
    """Display all transactions under the account owned by the user.

    [GET]   Display all transactions under an account.
    [POST]  Add transaction entry to the account.


    Args:
        account_id (int): the account id.

    Returns:
        HTML

    Raises:

    """
    return "transactions"

@app.route("/transactions/<int:transaction_id>" , methods=['GET','POST','GET'])
def transaction(transaction_id):
    """Display a single transaction using id.

    [GET]   Show record of transaction using id.
    [PUT]   Update the transaction using id.
    [DELETE] Delete the transaction using id.


    Args:
        transaction_id (int): the transaction id.

    Returns:
        HTML

    Raises:

    """
    return "transaction"
