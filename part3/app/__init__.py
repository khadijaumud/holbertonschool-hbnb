from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config_by_name

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    
    return app