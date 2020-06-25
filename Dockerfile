FROM jazzdd/alpine-flask:python3

RUN mkdir -p /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app /app

RUN make lint
