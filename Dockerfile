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

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Copy Supervisor configuration file
COPY supervisor.conf /etc/supervisor/conf.d/

# Create a directory for static files
RUN mkdir -p /app/static

# Collect static files
RUN python3 src/manage.py collectstatic --noinput

# Expose ports
EXPOSE 8000

CMD python3 src/manage.py runserver 0.0.0.0:8000 supervisord -n