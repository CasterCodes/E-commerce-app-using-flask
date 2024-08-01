from flask import Flask
from dotenv import load_dotenv
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

session = Session()

db = SQLAlchemy()

def create_app():
    load_dotenv()

    from .products import products
    from .auth import auth
    from .user import user
    from .cart import carts
    from .models import User
   
    app = Flask(__name__, template_folder='templates')
   
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('POSTGRES_CONNECTION_STRING')
    app.config['SQLALCMEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    app.config['SESSION_SQLALCHEMY'] = db 

   
    
    db.init_app(app=app)
    session.init_app(app=app)

    with app.app_context():
         db.create_all()
    
    app.register_blueprint(products,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(carts, url_prefix='/cart')

    
    login_manager = LoginManager()
    login_manager.login_view =  'auth.login'
    login_manager.init_app(app=app)


    @login_manager.user_loader
    def load_user(id):
         return User.query.get(int(id))
    

    return app