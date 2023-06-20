FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y libpq-dev gcc nginx supervisor

ENV PATH="/usr/lib/postgresql/2.9.6/bin:$PATH"

WORKDIR /app

COPY src/ .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Install gunicorn
RUN pip3 install gunicorn

# Collect static files
RUN python3 src/manage.py collectstatic --noinput

