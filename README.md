# flask-starter

Starting point for Flask projects, docker compose edition

## Usage

### Running tests

   docker compose -f compose-test.yaml build
   docker compose -f compose-test.yaml up

Runs `pytest` and `flake8` on host code (i.e., `.` is mounted as a volume).

### Development server

    docker compose build
    docker compose up

Launches a development server with live reload (i.e., `.` is mounted as a volume.) Edit away on local code,
and flask in the container will (should?) rebuild as needed.

The app is available on http://localhost:5000/

### Deploying

    docker compose -f compose-deploy.yaml build
    docker compose -f compose-deploy.yaml up

Builds a deploy. (This is speculative, and likely needs some work.)

The app is available on http://localhost:5000/
