FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y libpq-dev gcc

ENV PATH="/usr/lib/postgresql/2.9.6/bin:$PATH"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ .

CMD python src/manage.py runserver 0.0.0.0:8000
