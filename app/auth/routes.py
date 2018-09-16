from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm
from app.auth.user import User


@bp.route('/user')
def user():
    pass


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is not None and user.check_password(form.password.data):
            login_user(u, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('Invalid Username or Password.')
            redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(username=form.username.data)
        u.set_password(form.password.data)
        u.save()
        flash('You are now registered')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
