
import os
from flask import Flask
from dotenv import load_dotenv
from main.routes import main, poem, user

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')