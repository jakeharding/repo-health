/*
* repo-details.module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the module definition for the repo-details component
*/

import uiRouter from 'angular-ui-router';
import repoDetailsComponent from './repo-details.component';
import repoDetailsService from './repo-details.service';

const components = angular
  .module('components.repo-details', [uiRouter])
    .service('RepoDetailsService', repoDetailsService)
    .component('repoDetails', repoDetailsComponent)
  .run($api => {
    'ngInject';
      $api.add({
        resource: 'repo',
        url: '/'
      });
    })
  .name;

export default components;