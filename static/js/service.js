var app = angular.module('myApp');

app.factory('BrowserService', ['$window', function($window) {
  var BrowserService = {};

  BrowserService.isMobile = function() {
    return $($window).width() < 768;
  };

  BrowserService.isTablet = function() {
    return ($($window).width() >= 768) && ($($window).width() < 1160);
  };

  return BrowserService;
}]);