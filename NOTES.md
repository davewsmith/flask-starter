# flask-starter, docker compose edition

Moving on from the prior, Vagrant-based starter, because progress!

## Goals/waypoints

  * [done] Basic trivial app, deployable and dev-mode
  * pytest
  * Database, using current SQLAlchemy practices
  * Migrations
  * Local Auth
  * tailwindcss for dev-mode
  * Async jobs (probably celery)
    * With working logging

Loose ends:

  * 404, 400 handlers

Options:

  * Federatated Auth
  * HTMX

## Round 1

Fun docker edge case. Reused this repo name by renaming the old one and
creating a new one under the old name. `docker compose build` appeared
to work, but `docker compose up` brought up the old code. Deleting the
old image (via `docker image rm`) fixed things.

Haven't figured out how to get `gunicorn` to log requests. `--access-logfile`
doesn't seem to work. Maybe I'm holding it wrong.

The environments get rebuilt too often. There's probably a docker trick.
(And indeed, there way.)
