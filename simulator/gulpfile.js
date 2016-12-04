var gulp = require('gulp');
var browserify = require('browserify');
var source = require('vinyl-source-stream');

gulp.task('js', function(){
  browserify({
    entries: ['front/app.js']
  })
  .bundle()
  .on('error', function(err){
    console.log(err);
  })
  .pipe(source('app.js'))
  .pipe(gulp.dest('public/build'));
});
