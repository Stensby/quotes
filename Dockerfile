FROM jazzdd/alpine-flask:python3

RUN mkdir -p /app
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache --virtual .builddeps python3-dev libffi-dev openssl-dev musl-dev gcc
RUN pip install -r requirements.txt

COPY quotes /app

RUN flake8 --max-line-length 119 .

RUN apk del .builddeps
