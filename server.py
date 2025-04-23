import click

from app import create_app, db
from app.main.models import User


app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Add context variables for `flask shell`
    """
    return {
        # `app` is exported automagically
        'db': db,
        'User': User,
    }
