/*
* pull-req-stats.module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the module definition for the repo-details component
*/

import uiRouter from 'angular-ui-router';
import pullReqStatsComponent from './pull-req-stats.component';

const components = angular
  .module('components.pull-req-stats', [])
    // .service('PullReqStats', pullPreqStats)
    .component('pullReqStats', pullReqStatsComponent)
  .run($api => {
    'ngInject';
      $api.add({
        resource: 'pullReqStats',
        url: '/pull-requests'
      });
    })
  .name;

export default components;