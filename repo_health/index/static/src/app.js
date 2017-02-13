(function () {
  angular.module('repo-health', [
    'components'
  ])
  .config((function($locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise('/search');
  }));
})();
