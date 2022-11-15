from flask import Blueprint, render_template

poem = Blueprint('poem', __name__, url_prefix = 'poem')

@poem.route('/')
def index():
    return render_template('poem.html')

@poem.route('/poem:<id>')
def get_poem(id):
    return render_template('poem.html')


