(function () {
  var search = {
    templateUrl: '/static/src/components/search/search.html',
    controller: 'SearchController'
  };

  angular.module('components.search')
    .component('search', search)
    .config(function($stateProvider) {
      $stateProvider.state('search', {
        url: '/search',
        template: '<search></search>'
      });
  });
})();