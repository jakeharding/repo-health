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
import ngMaterial from 'angular-material';
import uiRouter from 'angular-ui-router';
import resources from './resources';
import components from 'components/components.module.js';
import mainComponent from './main.component';

//Styles
import 'global.css';

export const main = angular.module('repo-health', [
    uiRouter,
    ngMaterial,
    components,
    resources
  ])
  .component('main', mainComponent)
  .config(($locationProvider, $urlRouterProvider, $mdThemingProvider, $stateProvider) => {
    'ngInject';
    
    $locationProvider.hashPrefix('');
    $urlRouterProvider.otherwise('/search');
    $stateProvider.state('repo-health', {
        url: '/repo-health/:owner__login/:name',
        views: {
            'repo-details': {
                template: '<repo-details></repo-details>'
            },
            'pull-req-stats': {
                template: '<pull-req-stats></pull-req-stats>'
            }
        }
    })

    // Set-up themes
    $mdThemingProvider.theme('error').backgroundPalette('red').dark();

    $mdThemingProvider.theme('default')
      .primaryPalette('blue')
      .accentPalette('orange')
      .backgroundPalette('blue-grey');
  })
  .name;
