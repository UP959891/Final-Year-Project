#this file is for storing the routes a user can take navigating the website.

from flask import Blueprint

#Define this file is the BluePrint of this website

views = Blueprint('views', __name__) # dont need to name this the same as file

@views.route('/') #whenever the URL gets to the Home page this will run
def home():
    return "<h1>Test<h1/>"


