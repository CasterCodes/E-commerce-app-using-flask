from flask import render_template, Blueprint
from flask_login import login_required, current_user

user = Blueprint('user' , __name__)


@user.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)
    