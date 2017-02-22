/*
* app.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is where the angular app gets bootstraped.
* It will set up all the global configuration.
*/

(function () {
  angular.module('repo-health', [
    'components'
  ])
  .config((function($locationProvider, $urlRouterProvider) {
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise('/search');
  }));
})();
