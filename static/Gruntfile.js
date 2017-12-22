'use strict';

var jsFiles = [
  //'lib/modernizr/modernizr.js',
  'lib/jquery/jquery-2.1.1.js',
  'lib/angular/angular.js',
  'js/script.js',
  'js/app.js',
  'js/service.js',
  'js/directive.js',
  'js/controller.js'
];

var cssFiles = [
  'css/style.css'
];

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    cssmin: {
      combine: {
        files: {
          'dist/style.css': cssFiles
        }
      }
    },
    concat: {
      dist: {
        src: jsFiles,
        dest: 'dist/script.js'
      }
    },
    compass: {
      dist: {
        options: {
          config: 'config.rb'
        }
      }
    },
    uglify: {
      options: {
        mangle: false
      },
      dist: {
        src: '<%= concat.dist.dest %>',
        dest: 'dist/script.min.js'
      }
    },
    //imagemin: {
    //  dynamic: {
    //    files: [{
    //      expand: true,
    //      cwd: 'img/',
    //      src: ['**/*.{png,jpg,gif}'],
    //      dest: 'dist/img/'
    //    }]
    //  }
    //},
    watch: {
      css: {
        files: ['sass/*.scss'],
        tasks: ['compass', 'cssmin']
      },
      js: {
        files: jsFiles,
        tasks: ['concat', 'uglify']
      }
    },
    cachebreaker : {
      js: {
        asset_url : 'dist/script.min.js',
        files: {
          src : ['../templates/app/head.html']
        }
      },
      css: {
        asset_url : 'dist/style.css',
        files: {
          src : ['../templates/app/head.html']
        }
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  //grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-cache-breaker');

  // Default task.
  grunt.registerTask('default', ['compass', 'cssmin', 'concat', 'uglify', 'cachebreaker']);

};
