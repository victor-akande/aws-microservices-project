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
build:
	#build 
deploy:
	#deploy
all: install format lint test build deploy