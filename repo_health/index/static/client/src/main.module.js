/*
* main.module.js - (C) Copyright - 2017
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

import angular from 'angular';
import uiRouter from 'angular-ui-router';
import components from 'components/components.module.js';

//Styles
import 'global.css';

export const main = angular.module('repo-health', [
    uiRouter,
    components
  ])
  .config(($locationProvider, $urlRouterProvider) => {
    'ngInject';
    
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise('/search');
  })
  .name;
