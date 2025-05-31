FROM python:3.13-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN groupadd -g 1000 app && \
  useradd -m -d /app -s /bin/bash -u 1000 -g 1000 app && \
  chown app:app /app

WORKDIR /app
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

USER app
