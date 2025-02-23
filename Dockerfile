FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
apt-get install --no-install-recommends -y \
  python3-pip python3.10-venv && \
apt-get purge -y --auto-remove -o APT::AutoRemove:RecommendsImport=false && \
rm -rf /var/lib/apt-lists

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
