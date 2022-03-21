from flask import Blueprint,render_template,request,flash,url_for,redirect
from .models import User

from werkzeug.security import generate_password_hash,check_password_hash
from.import db
from flask_login import login_user,logout_user,current_user,login_manager,login_required
auth=Blueprint('auth' ,__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash("Login successfully",category='success')
                login_user(user,remember=True)
                return render_template(url_for("views.home"))
            else:
                flash("Incorrect password,try again.",category='error')
        else:
            flash("Email does not exist.",category='error')
    return render_template('login.html',user=current_user)
@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template(url_for('auth.login'))
@auth.route('/sign-up',methods=['GET','POST'])
def sign_up(): 
    if request.method=="POST":
        email=request.form.get('email')
        first_name=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        user=User.query.filter_by(email=email).first()
        if user :
            flash('Email already exist.',category='error')
        elif len(email)<4:
            flash("Email must be greater than 4 characters.",category='error')
        elif len('fistName')<2:
            flash('First name must be greater than 1 charaters.',category='error')
        elif password1!=password2:
            flash('Passwords don\'t match.',category='error') 
        elif len(password2)<7:
            flash('Password must be at least 7 characters.',category='error')
        else:
            #add user to database
            new_user=User(email=email,first_name=first_name,password=generate_password_hash(password1,method='sha256'))
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash('Account created!',category='success')
            return redirect(url_for('views.home'))
    return render_template('sign_up.html',user=current_user)
  