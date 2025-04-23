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
  * [done] Add database parts (with migrations) using SQLite3
  * [done] Add local auth
  * Add just enough styling
  * Add federated auth, using a development OIDC server
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


## Round 3

Add database and migration support, defaulting to sqlite3.

Added a User model. Made and applied the migration.

And, a complication. The migration looks to be database type specific.
This looks to complicate a scheme whereby local development uses SQLite3 and a
production deploy uses MySQL/PostgreSQL. This may mean commiting to a
database from the outset. If SQLite3, I'll need to look at how to mount
the .db file from the local filesystem, since having it in a Docker-managed
volume seems less than ideal.

Side quest: If SQLite3, when/were to enable WAL?

    pragma journal_mode=wal;

will return `wal` if enabled. For memory files (e.g., for testing), it will
return `memory`.

Next up, wire up auth with login/logout, and add a default user.

## Round 4

Pre-factor to put the database in a mounted directory with host-compatible
ownership (i.e., uid 1000, gid 1000).

## Round 5

Time for authentication, at least to the point of local login. Federated
login can wait a bit.

And, here comes the need to put up a skeleton UI, which pushes forward the
need to make some UI decisions. I hesitate here because CSS is where
I'm weakest. Choices here __feel, to me__ like they're hard to walk back.

But are they? Is there a way to slide that decision closer to easily
reversable (without becoming a lot better at CSS)? Backing up a step,
part of the purpose of this project is to gather up a starting point
for the next time an inspiration that calls for a webapp strikes.
And it's usually been the case that most layout/style decisions are
make in the primary (e.g, 'main') blueprint, and conformed to additional
blueprints.

So, why not provide a set of primary blueprints to choose from, where
each provides its own static files (which avoid name collision)? One
blueprint option would be traditional, another for HTMX, and so on.
The set will likely be small. Worth a try!

Added form support (`flask-wtf`) as an enabling step.

Until there's a better way, this works to create a User

```
$ flask shell
...
>>> from app.main.models import User
>>> from app import db
>>> u = User(username='admin', email='admin@example.com')
>>> u.set_password('admin')
>>> u
<User admin>
>>> db.session.add(u)
>>> db.session.commit()
>>> .q
```

## Round 5.1 a side trip into logging

One of these days I'll sort out how to configure Flask logging the way I want
it, but today isn't that day. https://flask.palletsprojects.com/en/stable/logging/
is at best misleading about default behavior.

## Round 6

O.K., let's add just enough styling.

Later, after slogging through PicoCSS and Tailwind tutorials and docs:
O.K., maybe later.

## Adding `flask shell` capability

```
$ docker exec -it flask-starter-web-1 /bin/sh
 * Tip: There are .env files present. Install python-dotenv to use them.
INFO made an app
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
App: app
Instance: /app/instance
>>> for u in q:
...     print(u.id, u.username, u.email)
... 
1 admin admin@example.com
>>>
```

