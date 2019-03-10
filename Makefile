setup:
	npm install

dev:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js

build:
	make dev
	lektor build --prune --output-path ${PWD}/public

watch:
	node_modules/gulp/bin/gulp.js sass:watch

deploy:
	make build
	rm -rf ${PWD}/public/.lektor
	rsync --progress -avc ${PWD}/public/ ${HOME}/Sites/fmartingr.com/

deploy_tests:
	bash tests/run.sh
