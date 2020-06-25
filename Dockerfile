FROM python:3-alpine

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache python3-dev libffi-dev openssl-dev musl-dev gcc make
RUN pip install -r requirements.txt

COPY . /app

RUN make lint
RUN make test

ENV PORT 80

CMD ["python3", "-m", "quotes.app"]
