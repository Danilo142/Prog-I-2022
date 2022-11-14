
from flask import Flask, Blueprint, render_template


app = Blueprint('app', __name__, url_prefix='/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html').format(title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html').format(title='Contact')

@app.route('/login')
def login():
    return render_template('login.html').format(title='Login')

@app.route('/register')
def register():
    return render_template('register.html').format(title='Register')

@app.route('/profile')
def profile():
    return render_template('profile.html').format(title='Profile')

@app.route('/logout')
def logout():
    return render_template('logout.html').format(title='Logout')

@app.route('/settings')
def settings():
    return render_template('settings.html').format(title='Settings')

@app.route('/admin')
def admin():
    return render_template('admin.html').format(title='Admin')

@app.route('/admin/users')
def admin_users():
    return render_template('admin_users.html').format(title='Admin Users')
