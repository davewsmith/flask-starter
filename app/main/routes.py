from flask import render_template

from app import db
from app.main import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('main/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('main/500.html'), 500


@bp.route('/')
def home():
    return render_template('main/home.html')


@bp.route('/fail')
def fail():
    raise Exception('This is what a fail looks like')
