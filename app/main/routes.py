from flask import render_template

from app.main import bp


@bp.route('/')
def home():
    return render_template('main/home.html')


@bp.route('/fail')
def fail():
    raise Exception('This is what a fail looks like')
