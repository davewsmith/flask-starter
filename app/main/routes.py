from flask import current_app, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa

from app import db
from app.main import bp
from app.main.forms import LoginForm
from app.main.models import User


@bp.route('/')
def home():
    return render_template('main/home.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    current_app.logger.info('not logged in')
    form = LoginForm()
    if form.validate_on_submit():
        # current_app.logger.debug(f"form.username.data = {form.username.data}")
        # current_app.logger.debug(f"form.password.data = {form.password.data}")
        query = sa.select(User).where(User.username == form.username.data)
        user = db.session.scalar(query)
        if user is None or not user.check_password(form.password.data):
            # TODO provide feedback
            return redirect(url_for('main.login'))
        login_user(user)
        current_app.logger.info(f'logged in {user.username}')
        return redirect(url_for('main.home'))
    return render_template('main/login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
