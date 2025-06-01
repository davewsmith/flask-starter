from flask.cli import with_appcontext

from app import create_app, db


app = create_app()


@app.cli.command(short_help="Create database")
@with_appcontext
def create_all():
    # Temporary hack until migrations are hooked up
    app.logger.info("db.create_all()"
                    f" on {app.config['SQLALCHEMY_DATABASE_URI']}")
    db.create_all()
