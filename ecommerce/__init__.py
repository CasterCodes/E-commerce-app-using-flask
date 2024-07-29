from flask import Flask
from dotenv import load_dotenv
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    load_dotenv()

    from .products import products
    from .auth import auth
    app = Flask(__name__, template_folder='templates')
   
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('POSTGRES_CONNECTION_STRING')
    app.config['SQLALCMEMY_TRACK_MODIFICATIONS'] = False

    from .models import User
    
    db.init_app(app=app)


    with app.app_context():
         db.create_all()
    
    app.register_blueprint(products,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    
    login_manager = LoginManager()
    login_manager.login_view =  'auth.login'
    login_manager.init_app(app=app)


    @login_manager.user_loader
    def load_user(id):
         return User.query.get(int(id))
    

    return app