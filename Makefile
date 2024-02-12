install:
	#install commands
		pip install --upgrade pip &&\
			pip install -r requirements.txt
post-install:
	python -m textblob.download_corpora			
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
run:
	# run docker container
	docker run -p 127.0.0.1:8080:8080 wiki-fastapi
deploy:
	#deploy
all: install post-install format lint test build run deploy