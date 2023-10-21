from flask import Flask,jsonify
from .config import Config

from .api import api

def create_app():
    app = Flask(__name__)
    print("1.................")
    app.config.from_object(Config)
    print("2.................")
    app.register_blueprint(api)
    print("3.................")
    @app.route('/')
    def index():
        context = {
            'status':True,
            'message':'principal'
        }
        return jsonify(context)
    
    return app