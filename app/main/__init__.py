from flask import Blueprint


bp = Blueprint('main', __name__, template_folder='templates')

from app.main import models  # noqa
from app.main import routes  # noqa
