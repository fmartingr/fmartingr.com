setup:
	pip install --user setuptools
	pip install --user poetry
	poetry install

clean:
	rm -rf public
	rm -rf assets/static/css

build:
	make clean
	poetry run lektor build -f scss --output-path ${PWD}/public --buildstate-path ${PWD}/.lektor
