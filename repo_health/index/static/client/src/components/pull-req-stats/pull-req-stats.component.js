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

import template from '../utils/base.template';

const pullReqStatsComponent = {
  template,
  bindings: {
    prStatsUrl: '='
  },
  controller: class pullReqStatsComponent {
    stats = null;
    charts = null;
    loadingStats = true;
    loadingMsg = "Loading pull request stats...";
    numOfStatsSections = 0;
    
    constructor( $http, $state, StatsService ) {
      'ngInject';
      Object.assign(this, { $http, $state, StatsService });
    }

    $onInit() {
      if (this.prStatsUrl) {
        this.StatsService.getStatsForUrl(this.prStatsUrl).then(stats => {
          this.stats = stats.metrics;
          this.charts = stats.charts;
          this.loadingStats = false;
          this.numOfStatsSections = this.StatsService.getRangeForSections(this.stats.length);
        });
      } else {
        this.$state.go('search', {
          error: true
        });
      }
    }
  }
};

export default pullReqStatsComponent;
