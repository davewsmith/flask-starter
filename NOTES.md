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

  * [done] Set up a basic flask application
  * Sort out mounting . inside the container
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

Things are set up to use a virtual environment inside the Dockerfile. Overkill?

## Round 2

Thinking about out how to make migrations. If made inside a container,
they need to be exfiltrated, which adds the complication of either mounting
source, or clumsiness in the form of a special exfil directory mounted as a
way to copy code back out. Thinking that doing migration development
outside of the container (i.e., using an activated virtual environment)
will be fine, so let's explore that.


