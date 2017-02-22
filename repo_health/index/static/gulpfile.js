const gulp = require('gulp');
const del = require('del');

gulp.task('default', ['static']);

gulp.task('static', ['clean'], () =>
  gulp.src([
    'client/assets/**/*'
  ], { base: './client' })
    .pipe(gulp.dest('dist'))
);

gulp.task('clean', function () {
  return del([ 'dist' ]);
});