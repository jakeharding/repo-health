/*
* pull-req-stats.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the creation of the pull-req-stats component.
*/

import template from './pull-req-stats';

const pullReqStatsComponent = {
  template,
  controller: class pullReqStatsComponent {
    stats = null;
    constructor(RepoDetailsService, $state, $stateParams, $repo) {
      'ngInject';
      Object.assign(this, {  RepoDetailsService, $state, $stateParams, $repo });
    }

    $onInit() {
      console.log(this.RepoDetailsService.repoDetails);
      // this.$repo.get('pullReqStats').then(stats => {
      //     this.stats = stats;
      // });
    }
  }
};

export default pullReqStatsComponent;
