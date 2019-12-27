from flask import render_template
from melvinperello_expense_story import app


@app.route("/" , methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/login" , methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/register" , methods=['GET'])
def register():
    return render_template('register.html')
