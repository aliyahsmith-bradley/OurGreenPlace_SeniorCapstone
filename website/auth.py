from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("auth/login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    data = request.form
    print(data)

    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordConfirmation = request.form.get('passwordConfirmation')  
 
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
            flash("Account created successfully.", category='success')  

    return render_template("auth/signup.html")