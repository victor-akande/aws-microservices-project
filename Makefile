install:
	#install commands
		pip install --upgrade pip &&\
			pip install -r requirements.txt
format:
	#format code using black
	black *.py mylib/*.py
lint:
	#lint code using pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib test_*.py
build:
	#build 
	docker build -t wiki-fastapi .
deploy:
	#deploy
all: install format lint test build deploy