'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var concatCss = require('gulp-concat-css');
var concatJs = require('gulp-concat');
var merge = require('merge-stream');
var minifyCss = require('gulp-minify-css');
var minify = require('gulp-minify');

gulp.task('sass', function() {
    var sassStream = gulp.src('./static/sass/style.sass')
        .pipe(sass().on('error', sass.logError));

    return merge(sassStream)
        .pipe(concatCss("style.css"))
        .pipe(minifyCss())
        .pipe(gulp.dest('./assets/static/css'));
});

gulp.task('js', function() {
    var jsStream = gulp.src([
        './static/js/main.js'
    ]);
    return jsStream
        .pipe(concatJs('app.js'))
        .pipe(minify({
            exclude: [],
            ignoreFiles: []
        }))
        .pipe(gulp.dest('./assets/static/js'))
})

gulp.task('sass:watch', function() {
    gulp.watch('./static/sass/*', gulp.parallel(['sass']));
});