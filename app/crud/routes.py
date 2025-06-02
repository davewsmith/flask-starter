from flask import render_template, redirect, url_for

import sqlalchemy as sa

from app import db
from . import bp
from .forms import CrudForm
from .models import Crud


@bp.route('/crud', methods=['GET', 'POST'])
def home():
    form = CrudForm()
    if form.validate_on_submit():
        new_crud = Crud(name=form.name.data)
        db.session.add(new_crud)
        db.session.commit()
        return redirect(url_for("crud.home"))

    query = sa.select(Crud)
    cruds = db.session.scalars(query).all()
    return render_template('crud/home.html', form=form, cruds=cruds)
