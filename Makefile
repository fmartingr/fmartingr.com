setup:
	npm install
	node_modules/bower/bin/bower install

dev:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js

build:
	make dev
	lektor build

watch:
	node_modules/gulp/bin/gulp.js sass:watch

deploy:
	make build
	lektor deploy

deploy_tests:
	bash tests/run.sh
