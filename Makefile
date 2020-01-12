setup:
	poetry install

dev:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js

build:
	make dev
	lektor build --prune --output-path ${PWD}/public

watch:
	node_modules/gulp/bin/gulp.js sass:watch

deploy_tests:
	bash tests/run.sh
