setup:
	poetry install
	npm install

build:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js
	lektor build --prune --output-path ${PWD}/public --buildstate-path ${PWD}/.lektor

watch:
	node_modules/gulp/bin/gulp.js sass:watch

deploy:
	make build
	rsync -e ssh --info=progress2 -r ${PWD}/public/ pages.sites.town:~/public_html/fmartingr.com/
