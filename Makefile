install:
	pip install -r requirements.txt

build_docker:
	docker build -t quote-api .

start: install
	python quotes/app.py

start_docker: build_docker
    docker run --rm -ti -p 80:80 quote-api

lint:
	flake8 .

.PHONY: install build_docker start start_docker lint test
