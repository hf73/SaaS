from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash #tool for hashing passwords
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() 
        if user:
            if check_password_hash(user.password, password): #checking if password is correct
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True) #remembers user is logged in as server is running
                return redirect(url_for('views.home')) #redirects to landing page(home)
            else:
                flash('Login Failed, Incorrect password!', category='error')

        else:
            flash('Email entered does not exist!', category='error') #email does not exist


    return render_template("login.html", boolean=True) #rendering the html template for login


@auth.route('/logout')
@login_required
def logout():
    logout_user #logs out user
    return redirect(url_for('auth.login')) #returns to login page after logout


@auth.route('/register' , methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')


        user = User.query.filter_by(email=email).first() # checking if user already exists
        if user:
            flash('Email is already registered! Try logging in.', category='error')
        elif len (email) < 6:
            flash('Email must be greater than 5 characters.', category='error')
        elif len(username) < 3:
            flash('First name must be greater than 3 character.', category='error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account successfully created!', category='success')
            return redirect(url_for('views.home')) #landing page after logging in

    return render_template("register.html", boolean=True) #rendering the html template for login