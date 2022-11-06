from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #helps to hash passwords
from . import db


auth = Blueprint('auth', __name__)

#added method to allow POST and GET requests, default only GET
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()#filters database and look by specific field, email
        if user:
            if check_password_hash(user.password, password): #hashes password and checks it against the hashed password
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again', category="error")
        else:
            flash('Email does not exists.', category='error')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': #forces differentiation between POST and GET method
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        #checks if email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        #checks length of email and returns error
        elif len(email) < 5:
            flash('Email must be greater than 5 characters', category='error')
        #checks length of username and returns error
        elif len(username) < 3:
            flash('Username must be greater than 3 characters', category='error')
        #checks length of password and returns error    
        elif len(password) < 6:
            flash('Password must be greater than 6 characters', category='error')
        else:
            #add user to database. hash password as sha256 hashing algorithm
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
           
            db.session.add(new_user) #adds user to the database
            db.session.commit() #commits the user to the database
            flash('Successfully created account!', category='success')
           
            #redirects to landing page (home page)
            return redirect(url_for('views.home')) 

    return render_template("register.html")
