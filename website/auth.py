from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

#added method to allow POST and GET requests, default only GET
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form #has all the data that was sent as a form, such as email and pass
    print(data)
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

        if len(email) < 5:
            flash('Email must be greater than 5 characters', category='error')
        elif len(username) < 3:
            flash('Username must be greater than 3 characters', category='error')
        elif len(password) < 6:
            flash('Password must be greater than 6 characters', category='error')
        else:
            #add user to database
            flash('Successfully created account!', category='success')

    return render_template("register.html")
