setup:
	npm install

dev:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js

build:
	make dev
	lektor build --output-path ./public -f htmlmin

watch:
	node_modules/gulp/bin/gulp.js sass:watch

deploy:
	make build

deploy_tests:
	bash tests/run.sh
