# Notes

O.K. then, time to move from a Vagrant/Virtualbox development
environment to a `docker compose` one.

## GOALS

  * Gather up a starting point for a production-ready, containerized
    Flask application that supports federated authentication and
    asyncronous tasks
  * Sort out how to do zero-downtime migrations

## NON-GOALS

  * Support for any specific application
  * Make it pretty

## TO DO

In roughly this order:

  * [done] Set up a basic flask application
  * [nope] Sort out mounting . inside the container
  * [done] Set up tests and flake8
  * Run tests and flake8 from a github action
  * Add database parts (with migrations) using SQLite3
  * Add auth, using a development OIDC server
  * Put the app behind gunicorn
  * Asynchronous task support (celery, redis)

Optional:

  * coverage
  * Add MySQL or PostgreSQL support
  * Pick a CSS framework
  * HTMX
  * Sort out how to deploy internally behind tailscale

## Round 1

A minimal starting point

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
FLASK_APP=server.py flask run
```

Then visit `http://localhost:5000`

or

```
docker compose build
docker compose up
```

Then visit `http://localhost:5000`

Things are set up to use a virtual environment inside the Dockerfile. Overkill?

## Round 2

Thinking about out how to make migrations. If made inside a container,
they need to be exfiltrated, which adds the complication of either mounting
source, or clumsiness in the form of a special exfil directory mounted as a
way to copy code back out. Thinking that doing migration development
outside of the container (i.e., using an activated virtual environment)
will be fine, so let's explore that.

Since MySQL supports a wider ranges of schema changes than SQLite3,
this may speak to adding MySQL into the mix.

Remapped the flask port such that the compose environment serves from :8000,
and verified that a local run (on :5000) can co-exist, at least for the moment.

Flake8, because of course. And oh, right. `conftest.py` is where the fixtures
go.

On to (simple) database and migrations.

Thinking also that it might be time to drive this from github issues,
but on the other hand, that feels like Jira, and f\*ck that.

## Round 2.1

Made a simple starting point on layout and styles.
The base app defines `app/templates/base.html`, which uses a starter
stylesheet owned in `app/static/`. The `main` blueprint extends that.

A thought: Maybe a `layouts` blueprint, with a set of ~base starting points
for different UIs.

... or, maybe, the layout options live in `app/templates/`, since
they'll be matched with CSS in `app/static/`

