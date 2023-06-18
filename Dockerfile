FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y libpq-dev gcc nginx supervisor

ENV PATH="/usr/lib/postgresql/2.9.6/bin:$PATH"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/manage.py .


# Copy NGINX and Supervisor configuration files
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisor.conf /etc/supervisor/conf.d/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose ports
EXPOSE 8000

CMD python src/manage.py runserver 0.0.0.0:8000 supervisord -n
