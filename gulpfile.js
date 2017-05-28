"use strict";

var gulp = require("gulp");
var babel = require("gulp-babel");

gulp.task("build", function () {
    return gulp.src(["**/*.js", "!node_modules/**/*.js"]).pipe(babel({
        presets: ['es2015'],
    }))
    .pipe(gulp.dest("."));
});