from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

#added method to allow POST and GET requests, default only GET
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")
