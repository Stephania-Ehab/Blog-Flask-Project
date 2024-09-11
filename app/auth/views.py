from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm
from app.models import db, User
from werkzeug.security import generate_password_hash
from app.auth import auth_blueprint


##################### Register #####################
@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations...Registration done!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('author/register.html', form=form)


##################### Login #####################
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('posts_landing'))
        flash('Invalid username or password', 'danger')
    return render_template('author/login.html', form=form)


# ##################### Logout #####################
# @auth_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))
