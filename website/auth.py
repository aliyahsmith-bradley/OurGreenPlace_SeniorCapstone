from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    from .models import User

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login successful.", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password. Try again.", category='error')
        else:
            flash("Email does not exist.", category='error')

    return render_template("auth/login.html", boolean=True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    from .models import User, db
    
    # Retrieves user data from sign up form 
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordConfirmation = request.form.get('passwordConfirmation')  
         
        user = User.query.filter_by(email=email).first()

        # Validates user input before submission
        if user:
            flash("Email already exists.", category='error')
        elif firstName is None or len(firstName) < 2:
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
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(firstName=firstName, lastName=lastName, email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created successfully.", category='success')  
            return redirect(url_for('views.home'))

    return render_template("auth/signup.html")