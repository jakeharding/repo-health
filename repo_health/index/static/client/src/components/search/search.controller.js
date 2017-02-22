/*
* search.controller.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the controller that will be used in the search component.
* It will allow a user to search on a repo
*/

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