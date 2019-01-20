from .. import db
from flask import Blueprint, render_template, request,redirect,url_for,flash,session,current_app
from flask_login import current_user, login_user, logout_user, login_required
from app.models.user import User,Role
from .forms import LoginForm, UserSignUp
from flask_login import login_user
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth', __name__)

Administrator = 'Administrator' 
doc = 'Doctor'
@auth.route('/login' , methods = ['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate(): 
        user = User.query.filter_by(username=form.username.data).first() 
        print(user)
        role = Role.query.filter_by(id=user.role_id).first()
        print('role')
        print(role.name)
        if user is None: 
            flash("user does not exist") 
        elif not (user.password,form.password.data): 
            flash("userp ee does not exist")
            return render_template('accounts/login.html',form=form) 
        else: 
            #current_app('User login: %s\n' % user.username)
            flash("welcome back")


            user.authenticated = True
            #user.current_sign_in_ip(request.remote_addr)
            user.last_logged_in = user.current_logged_in
            user.current_logged_in = datetime.now()
            print(user.username)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            if role.name == Administrator:
                print("welcome Administrator")
                return redirect(url_for('admin.index',username=current_user.username))


            elif role.name == doc:
                print("welcome Administrator")
                return redirect(url_for('doctor.index',username=current_user.username))

            else:
                return redirect(url_for('patient.index', username=current_user.username))    
     
    return render_template('accounts/login.html',form=form)
 
 



@auth.route('/logout')
@login_required
 
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye!', 'info')
    return redirect(url_for('main.index'))

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    form2 = UserSignUp(request.form)
    if request.method == 'POST' and form2.validate():
    
        new_user = User(username=form2.username.data,email=form2.email.data,password=form2.password.data,phone=form2.phone.data,fullname=form2.fullname.data)
        new_user.authenticated = True
        new_user.role_id = 1


        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        session['username'] = request.form['username']
        flash("successful signup ")
        return redirect(url_for('patient.index',username=current_user.username))

    return render_template('accounts/signup.html',form=form2)
