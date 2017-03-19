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
    loadingStats = true;
    loadingMsg = "Loading issue stats..."
    constructor(RepoDetailsService, $state, $stateParams, $repo) {
      'ngInject';
      Object.assign(this, {  RepoDetailsService, $state, $stateParams, $repo });
    }

    $onInit() {
      console.log(this.RepoDetailsService.repoDetails);
      if(this.RepoDetailsService.repoDetails) {
          let params = {
            id: this.RepoDetailsService.repoDetails.id,
            verb: 'pull-requests'
          }
          this.$repo.get('pullReqStats', params).then(stats => {
              this.stats = stats;
          });
      }
    }
  }
};

export default pullReqStatsComponent;
