from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Samer/Desktop/AUB/EECE 503M/Sport_store/dbapplication/testdb.db'
    app.secret_key = 'Some Key'
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    from models import User
    
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app)
    
    from routes import register_routes
    register_routes(app, db,bcrypt)
    
    migrate = Migrate(app, db)
    
    return app