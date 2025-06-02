from flask import render_template, redirect, url_for

import sqlalchemy as sa

from app import db
from . import bp
from .models import Crud


@bp.route('/crud')
def home():
    query = sa.select(Crud)
    cruds = db.session.scalars(query).all()
    return render_template('crud/home.html', cruds=cruds)


@bp.route('/crud/add')
def add():
    db.session.add(Crud(name="More Crud!"))
    db.session.commit()
    return redirect(url_for("crud.home"))
