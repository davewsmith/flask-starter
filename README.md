# Flask Starter

A skeletal Flask application that uses `docker compose` to set up
a simulated live environment.

## Local development

    python -m venv venv
    pip install -r requirements.txt
    FLASK_APP=server venv/bin/flask run

Brings up the web server on `http://localhost:5000/`

## Simulated deployment

    docker compose build
    docker compose up

Brings up an environment, with the web server on `http://localhost:5000`

    docker exec -it flask-starter-web-1 /bin/bash

gets a shell in the web server.
