/*
* search.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the creation of the search component.
*/

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