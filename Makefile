setup:
	npm install
	node_modules/bower/bin/bower install

dev:
	node_modules/gulp/bin/gulp.js sass
	node_modules/gulp/bin/gulp.js js

watch:
	node_modules/gulp/bin/gulp.js sass:watch
