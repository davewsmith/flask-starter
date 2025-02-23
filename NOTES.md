# Notes

O.K. then, time to move from a Vagrant/Virtualbox development
environment to a `docker compose` one.

## GOALS

 * Gather up a starting point for a production-ready, containerized
   Flask application that supports federated authentication

## NON-GOALS

  * Support for any specific application
  * Make it pretty

## TO DO

In roughly this order:

  * Set up a basic flask application
  * Set up tests and run them from a github action
  * Add database parts (with migrations) using SQLite3
  * Add celery, using redis
  * Add auth, using a development OIDC server
  * Put the app behind gunicorn

Optional:

  * Pick a CSS framework
  * Add MySQL or PostgreSQL support
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
