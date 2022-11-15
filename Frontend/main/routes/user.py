from flask import Blueprint, render_template, request

author = Blueprint('author', __name__, url_prefix = 'author')

@author.route('/')
def index():
    return render_template('index.html')

@author.route('/author:<id>')
def profile(id):
    return render_template('user_profile.html')


