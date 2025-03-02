from flask import render_template, redirect, url_for

from app.main import bp
from app.main.forms import LoginForm


@bp.route('/')
def home():
    return render_template('main/home.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('main/login.html', form=form)


@bp.route('/logout')
def logout():
    return redirect(url_for('main.home'))
