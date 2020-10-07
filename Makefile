setup:
	pip install --user setuptools
	pip install --user poetry
	poetry install
	npm install

build:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js
	poetry run lektor build --prune --output-path ${PWD}/public --buildstate-path ${PWD}/.lektor

watch:
	node_modules/gulp/bin/gulp.js sass:watch
