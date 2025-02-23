FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
apt-get install --no-install-recommends -y \
  python3-pip && \
apt-get purge -y --auto-remove -o APT::AutoRemove:RecommendsImport=false && \
rm -rf /var/lib/apt-lists

WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
