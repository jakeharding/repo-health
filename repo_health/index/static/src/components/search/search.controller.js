(function () {
  angular.module('components.search')
    .controller('SearchController', SearchController);

  function SearchController() {
    var ctrl = this;

    ctrl.getStats = function() {
      // Add service to get the statistics
    }
  }
})();