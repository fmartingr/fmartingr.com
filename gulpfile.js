'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var concatCss = require('gulp-concat-css');
var merge = require('merge-stream');
var minifyCss = require('gulp-minify-css');

gulp.task('sass', function() {
    var sassStream = gulp.src('./static/sass/style.sass')
        .pipe(sass().on('error', sass.logError));

    return merge(sassStream)
        .pipe(concatCss("style.css"))
        .pipe(minifyCss())
        .pipe(gulp.dest('./assets/static/css'));
});

gulp.task('sass:watch', function() {
    gulp.watch('./static/sass/*', gulp.parallel(['sass']));
});
