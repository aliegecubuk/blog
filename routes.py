from flask import Blueprint, render_template, request, session, redirect
from user.models import User, get_db

user_bp = Blueprint('user_data', __name__)

# Other routes...

@user_bp.route('/user/signup', methods=['POST'])
def signup():
    user_data = User()
    response = user_data.signup()
    return response

@user_bp.route('/user/signout')
def signout():
    return User().signout()

@user_bp.route('/user/login', methods=['POST'])
def login():
    return User().login()

@user_bp.route('/user/make_post')
def make_post():
    if 'user' in session:
        return render_template('make_post.html')
    else:
        return redirect('/')

@user_bp.route('/user/create_post', methods=['POST'])
def create_post():
    return User().create_post()

@user_bp.route('/user/profile')
def profile():
    if 'user' not in session:
        return redirect('/')
    
    user_email = session['user']['Email']
    user = get_db().your_db.find_one({"Email": user_email})
    return render_template('profile.html', user=user)
