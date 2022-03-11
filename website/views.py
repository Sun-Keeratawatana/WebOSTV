from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'