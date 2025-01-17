# Designer Defined
from contactapp import app, db, mail, bcrypt
from contactapp.database import User, Contacts
from contactapp.forms import (Registrationform, Loginform, UpdateAccountForm,
                              RequestResetForm, RequestPasswordForm)

# pre-defined
import os
import secrets
from PIL import Image
from functools import wraps
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user, login_user, logout_user
from datetime import timedelta
from sqlalchemy import or_
from flask_mail import Message


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('Login'))

    return wrap


@app.route('/', methods=["POST", "GET"])
@app.route('/Login', methods=["POST", "GET"])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('Homepage'))
    form = Loginform()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if user.password == form.password.data:
                session.update({'id': user.id})
                flash('Welcome! ' + 'successfully logged in as ' + form.email.data, 'success')
                x = user.contacts
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else render_template('Homepage.html', title='Homepage',
                                                                             contacts=x)
            else:
                flash('Wrong Password')
                return render_template('login.html', title='Login', form=form)
        except AttributeError:
            flash('Wrong Username')
            return render_template('login.html', title='Login', form=form)
    else:
        return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.email.data}!", "success")
        return redirect(url_for('Login'))
    return render_template('register.html', title=register, form=form)


@app.route('/Homepage', methods=["POST", "GET"])
@login_required
def Homepage():
    x = Contacts.query.filter_by(user_id=session['id']).all()
    return render_template('Homepage.html', title='Homepage', contacts=x)


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=["POST"])
@login_required
def insert():
    if request.method == "POST":
        name = request.form['contact_name']
        email = request.form['contact_mail']
        phone = request.form['mobile_number']
        contact = Contacts(number=phone, contact_name=name, contact_mail=email, user_id=session['id'])
        db.session.add(contact)
        db.session.commit()
        flash("Contact Inserted Successfully")
        return redirect(url_for('Homepage'))


# this is our update route where we are going to update our contact

@app.route('/update/<int:id11>', methods=["POST"])
@login_required
def update(id11):
    print(request.method, request.form.items())

    if request.method == 'POST':
        id1 = request.form['id']
        name = request.form['contact_name']
        email = request.form['contact_mail']
        phone = request.form['mobile_number']
        up = Contacts.query.get(id1)
        up.contact_name = name
        up.contact_mail = email
        up.number = phone
        db.session.commit()
        x = Contacts.query.all()
        print(x)
        flash("Contact Updated Successfully")
        return redirect(url_for('Homepage'))


# This route is for deleting our contact
@app.route('/delete/<string:number>', methods=["POST", "GET"])
@login_required
def delete(number):
    dele = Contacts.query.get(number=number)
    db.session.delete(dele)
    db.session.commit()
    flash("Contact Deleted Successfully", 'danger')
    return redirect(url_for('Homepage'))


@app.route('/search', methods=['POST', 'GET'])
@login_required
def search():
    if request.method == 'POST':
        search_for = request.form['searchDB']
        print(search_for)
        search_value = "%{}%".format(search_for)
        results = Contacts.query.filter(or_(Contacts.contact_name.like(search_value),
                                            Contacts.number.like(search_value)), user_id=session['id']).all()
        print(results)
        return render_template('Homepage.html', contacts=results)
    else:
        flash('No results found')
        return redirect(url_for('Homepage'))


@app.route('/Logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('Login'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account_info", methods=['GET', 'POST'])
@login_required
def account_info():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account_info'))
    elif request.method == 'GET':
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account_info.html', title='Account',
                           image_file=image_file, form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Verification', sender='mady4485@gmail.com', recipients=[user.email])
    msg.body = f''' This an machine generated email to reset your Account {user.email}. 
To reset Your Account Password Please click the link provided{url_for('reset_token', token=token, _external=True)}

If you did not click to reset Just simply IGNORE the mail and no credentials will be Changed for Your account '''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('Homepage'))
    form = RequestResetForm()
    if form.validate_on_submit():
        print(form.email.data)
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        send_reset_email(user)
        flash(f"An Mail has been sent to {form.email.data}", 'info')
        return redirect(url_for('Login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('Homepage'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token..', 'warning')
        return redirect(url_for('reset_request'))
    form = RequestPasswordForm()
    if form.validate_on_submit():
        user.password = form.password.data
        db.session.commit()
        flash('Your Password has been updated. You will be able to login from now', 'success')
        return redirect(url_for('Login'))
    return render_template('reset_password.html', title='Reset Password', form=form)
