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

import template from '../base-component/base.template';

const pullReqStatsComponent = {
  template,
  bindings: {prStatsUrl: '='},
  controller: class pullReqStatsComponent {
    stats = null;
    loadingStats = true;
    loadingMsg = "Loading issue stats..."
    constructor(RepoDetailsService, $state, $stateParams, $http) {
      'ngInject';
      Object.assign(this, { RepoDetailsService, $state, $stateParams, $http });
    }

    $onInit() {
        this.$http.get(this.prStatsUrl).then(stats => {
            this.stats = stats.data;
            this.loadingStats = false;
        })
      // this.RepoDetailsService.getStats(this.$stateParams).then( () => {
      //     let params = {
      //       id: this.RepoDetailsService.repoDetails.id,
      //       verb: 'pull-requests'
      //     }
      //     this.$repo.get('pullReqStats', params).then(stats => {
      //         this.stats = stats;
      //         this.loadingStats = false;
      //       }, () => {this.$state.go('search')}
      //     );
      // });
    }
  }
};

export default pullReqStatsComponent;
