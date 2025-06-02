from flask import Blueprint

bp = Blueprint('crud', __name__, template_folder='templates')

from . import routes  # noqa
from . import models  # noqa
