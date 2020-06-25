install:
	pip install -r requirements.txt

build_docker:
	docker build -t quotes-api .

start: install
	python -m quotes.quotes

start_docker: build_docker
	docker run --name quotes-api --rm -ti -p 80:80 quotes-api

lint:
	flake8 --max-line-length 119 .

test:
	coverage run -m unittest
	coverage report --include 'quotes/tests/*'

.PHONY: install build_docker start start_docker lint test
