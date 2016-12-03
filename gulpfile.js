'use strict';

var gulp = require('gulp');

// Styles
var sass = require('gulp-sass');
var concatCss = require('gulp-concat-css');
var concatJs = require('gulp-concat');
var merge = require('merge-stream');
var minifyCss = require('gulp-minify-css');
var livereload = require('gulp-livereload');
var yargs = require('yargs').argv;
var minify = require('gulp-minify');


gulp.task('sass', function () {
  var sassStream = gulp.src('./assets/static/sass/style.scss')
             .pipe(sass().on('error', sass.logError))
  var bowerStream = gulp.src([
    ])

  return merge(bowerStream, sassStream)
         .pipe(concatCss("style.css"))
         .pipe(minifyCss())
         .pipe(gulp.dest('./assets/static/css'))
         .pipe(livereload());
});

gulp.task('js', function () {
  var bowerStream = gulp.src([
    './bower_components/google-code-prettify/bin/run_prettify.min.js'
  ])
  return bowerStream
         .pipe(concatJs('app.js'))
         .pipe(minify({
           exclude: [],
           ignoreFiles: []
         }))
         .pipe(gulp.dest('./assets/static/js'))
})

gulp.task('livereload', function () {
  return gulp.src('./templates/**/*.html').pipe(livereload());
});

gulp.task('sass:watch', function () {
  livereload.listen();
  gulp.watch('./templates/static/sass/**/*.scss', ['sass']);
  gulp.watch('./templates/static/templates/**/*.html', ['livereload']);
});