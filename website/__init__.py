import os
from dotenv import load_dotenv
from flask import Flask
load_dotenv()

app = Flask(__name__)

def create_website():
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .views import views
    app.register_blueprint(views, urkl_prefix = "/")


    return app