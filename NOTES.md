# flask-starter, docker compose edition

Moving on from the prior, Vagrant-based starter, because progress!

## Goals/waypoints

  * [done] Basic trivial app, deployable and dev-mode
  * [done] pytest and flake8
  * [done] tailwindcss for dev-mode
  * [done] Database, using current SQLAlchemy practices
  * Migrations
  * Local Auth
  * Async jobs (probably celery)
    * With working logging

Loose ends:

  * [done] 404, 400 handlers
  * Cache-bust CSS

Options:

  * Federated Auth
  * HTMX
  * Maybe Tailwind CDN as an option, though that's entirely a
    template thing, and can co-existing with wasting memory and
    cycles running the cli
  * [in progress] A CRUD Blueprint, mostly to have a starting point for forms,
    pagination, and such

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

## Round 3.1 - 404 and 500

Adding handlers for these is forcing the issue of HTML structure.
Thinking that I might have been overthinking this in the past.
The idea of having a special 'layout' Blueprint sounded good
in theory, but in practice all of the code-bearing Blueprints
need their templates to conform to layout anyway, so it might
as well go in a trimmed-down main Blueprint.

Consulting https://flask.palletsprojects.com/en/stable/blueprints/#templates for clarity.

Maybe I wasn't overthinking it. Good thing decisions here aren't final.

## Round 4 - Database

Volume foibles. Create it in the Dockerfile first so that the mounted
volume will have the right ownership. Brought to you by a cryptic
SQLAlchemy failure when /data was owned by root:root

Now the question: To demo db hookup, and actually, you know, add a
table and do a query, add Auth next, or CRUD next?

CRUD, since a few project I intend this for won't need Auth.

Getting wtforms and tailwindcss to play well together might require
some arm-wrestling.

Needs pagination and delete, but that's good for this round.

## Interlude

"If this were Django, I'd be done by now."

Questioning my choice of Flask for future projects. It's been a
good run, but looking around in the ecosystem and poking around
at issues and PRs in various Flask dependencies, I get the
sense that Flask world is held together by a splintering group of
developers. Finding the issue and PR I filed against Flask-Testing
seven years ago sitting there isn't helping, even if that's
now not the recommended way to test. Do I want to be spending
time tending updates within the ecosystem?

Parking this for now.
