/*
* search.module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the module definition for the search component
*/

import uiRouter from 'angular-ui-router';
import searchComponent from './search.component';

const components = angular
  .module('components.search', [uiRouter])
    .component('search', searchComponent)
    .config($stateProvider => {
      'ngInject';

      $stateProvider.state('search', {
        url: '/search',
        template: '<search></search>',
        params: {
          error: false
        }
      })
    })
  .name;

export default components;