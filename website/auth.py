from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

#function to check if password contains at least one number
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


#login authorisation function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #get email and password from login form
        email = request.form.get('email')
        password = request.form.get('password')

        #check if user exists
        user = User.query.filter_by(email=email).first()
        if user:
            #check that user's password matches hashed stored password
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                #if password is correct log user in to home page
                return redirect(url_for('views.home'))
            else:
                #notify if user inputs incorrect password
                flash('Incorrect password, try again.', category='error')
        else:
            #notify if email not in system
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


#logout function
@auth.route('/logout')
#require user to be logged in to see this option
@login_required
def logout():
    #use flask's in built logout manager
    logout_user()
    return redirect(url_for('auth.login'))


#sign up function
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #set email, first name, password and confirmed password to user inputs from form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        #check that email is longer than 3 chars
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        #check that first name is longer than one char
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        #check if password and confirm password match
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        #check that password length is at least 10 characters
        elif len(password1) < 10:
            flash('Password must be at least 10 characters.', category='error')
        #check that password contains at least one number
        elif containsNumber(password1) == False:
            flash('Password must contain at least one number.', category='error')
        #if all checks pass then create a new user and add to database
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #login the new user
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)