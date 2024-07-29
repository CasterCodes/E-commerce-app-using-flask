
from flask import Blueprint, render_template,request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
from sqlalchemy.exc import SQLAlchemyError
from .models import User
from . import db


auth  = Blueprint('auth', __name__)

@auth.route("/register", methods=['POST', 'GET'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get("email")
        password = request.form.get('password')
        confirm_password = request.form.get("confirmPassword")

      
        # Basic validation
        if not username or len(username) < 2 or len(username) > 20:
            flash("Username must be between 2 and 20 characters long.", 'danger')
        elif not email or '@' not in email:
            flash("Invalid email address.", 'danger')
        elif not password or len(password) < 6:
            flash("Password must be at least 6 characters long.", 'danger')
        elif password != confirm_password:
            flash("Passwords do not match.", 'danger')
        elif User.query.filter_by(email=email):
            flash('Email taken')
        else:
            
            new_user = User(email=email, username=username, password=generate_password_hash(password))

            try:
                 db.session.add(new_user)
                 db.session.commit()
                 flash(f'Account created for {username}!', 'success')
                 return redirect('/auth/login')
            except SQLAlchemyError as e:
                print(f'Error: {e}')
                flash(f"Oops! an error occured!!!.", 'danger')
           
           
    return render_template('signup.html')




@auth.route("/login", methods=['POST', 'GET'])
def login():  
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get('password')

        if not email or not password:
            flash('Please provde all login credentials', 'danger')
        else:
           user = User.query.filter_by(email=email).first()

           if not user or not check_password_hash(user.password, password):
                flash('Invalid login credentials', 'danger')
           else:
                login_user(user=user, remember=True)
                return redirect('/')
                
    return render_template('login.html')


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('products.index'))


  

