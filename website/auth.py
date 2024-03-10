from flask import Blueprint, render_template, request, flash, redirect, url_for
#from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #Testing -- prints login form data
    data = request.form
    print(data)
    return render_template("auth/login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # Testing -- prints sign up form data 
    data = request.form
    print(data)

    # Retrieves user data from sign up form 
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordConfirmation = request.form.get('passwordConfirmation')  
 
        # Validates user input before submission 
        if firstName is None or len(firstName) < 2:
            flash("First name must be greater than 1 character.", category='error') 
        elif lastName is None or len(lastName) < 2:
            flash("Last name must be greater than 1 character.", category='error') 
        elif email is None or len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error') 
        elif username is None or len(username) < 2:
            flash("Username must be greater than 1 character.", category='error') 
        elif password is None or len(password) < 6:
            flash("Password must be greater than 5 characters.", category='error')
        elif password != passwordConfirmation:
            flash("Passwords do not match.", category='error')  
        else:
            # Creates new user and adds account to database 
            from .models import User, db
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(firstName=firstName, lastName=lastName, email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully.", category='success')  
            return redirect(url_for('views.home'))

    return render_template("auth/signup.html")