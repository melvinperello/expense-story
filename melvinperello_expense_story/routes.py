from flask import render_template, url_for, flash, redirect, request
from melvinperello_expense_story import app
from melvinperello_expense_story.forms import LoginForm , RegisterForm, FundsAddForm
from melvinperello_expense_story.controllers import LoginController , RegisterController
from flask_login import current_user, logout_user, login_required

@app.route("/" , methods=['GET'])
def home():
    """Display the home page.

    [GET]   This will display the main view of the application.

    Args:

    Returns:
        HTML

    Raises:

    """
    if current_user.is_authenticated:
        return redirect(url_for('funds'))
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
    if current_user.is_authenticated:
        return redirect(url_for('funds'))

    form = LoginForm()
    if form.validate_on_submit():
        # form is valid
        # proceed authentication
        controller = LoginController()
        controller.username = form.username.data
        controller.password = form.password.data
        controller.remember = form.remember.data

        if controller.authenticate():
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('funds'))
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
    if current_user.is_authenticated:
        return redirect(url_for('funds'))
    form = RegisterForm()
    if form.validate_on_submit():
        controller = RegisterController()
        controller.username = form.username.data
        controller.password = form.password.data
        if controller.register():
            flash('Account successfully created !', 'success')
            return redirect(url_for('login'))
        else:
            flash('Something went wrong while creating the account.', 'danger')
    return render_template('register.html', form=form)



@app.route("/funds" , methods=['GET','POST'])
@login_required
def funds():
    """Display all funds owned by the user.

    [GET]   Display all funds for the user.
    [POST]  Add fund to the user.

    Args:


    Returns:
        HTML

    Raises:

    """
    form = FundsAddForm()
    if form.validate_on_submit():
        pass
    return render_template('funds.html', form=form)

@app.route("/funds/<int:fund_id>" , methods=['GET','PUT','DELETE'])
@login_required
def fund(fund_id):
    """Display a specific fund owned by the user.

    [GET]   Display the fund using the fund id.
    [PUT]   Update the fund using the fund id.
    [DELETE] Delete the fund using the fund id.

    Args:
        fund_id (int): the fund id.

    Returns:
        HTML

    Raises:

    """
    return "fund"

@app.route("/transactions/funds/<int:fund_id>" , methods=['GET','POST'])
@login_required
def transactions(fund_id):
    """Display all transactions under the fund owned by the user.

    [GET]   Display all transactions under an fund.
    [POST]  Add transaction entry to the fund.


    Args:
        fund_id (int): the fund id.

    Returns:
        HTML

    Raises:

    """
    return "transactions"

@app.route("/transactions/<int:transaction_id>" , methods=['GET','POST','GET'])
@login_required
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
