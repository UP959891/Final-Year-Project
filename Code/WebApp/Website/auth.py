from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/logout')
def home():
    return "<h1>you have Logged out</h1>"

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/sign-up')
def signup():
    return render_template('sign_up.html')