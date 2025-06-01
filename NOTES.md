# flask-starter, docker compose edition

Moving on from the prior, Vagrant-based starter, because progress!

## Goals/waypoints

  * [done] Basic trivial app, deployable and dev-mode
  * [done] pytest and flake8
  * [done] tailwindcss for dev-mode
  * Database, using current SQLAlchemy practices
  * Migrations
  * Local Auth
  * Async jobs (probably celery)
    * With working logging

Loose ends:

  * 404, 400 handlers

Options:

  * Federatated Auth
  * HTMX
  * Maybe Tailwind CDN has an option, though that's entirely a
    template thing, and can co-existing with wasting memory and
    cycles running the cli.

## Round 1 - Simple App

Fun docker edge case. Reused this repo name by renaming the old one and
creating a new one under the old name. `docker compose build` appeared
to work, but `docker compose up` brought up the old code. Deleting the
old image (via `docker image rm`) fixed things.

Haven't figured out how to get `gunicorn` to log requests. `--access-logfile`
doesn't seem to work. Maybe I'm holding it wrong.

The environments get rebuilt too often. There's probably a docker trick.
(And indeed, there was.)

## Round 2 - pytest and flake8

Reminded that flask8 doesn't speak pyproject.toml

Also, happy to finally shake off Flask-Testing, which hasn't been updated
in years.

## Round 3 - tailwindcss

After realizing that tailwindcss was (or could be) part of the dev environment
as it currently is, let's do that next. Requires some theory of how to structure
HTML, but that's easy enough to revisit later.

