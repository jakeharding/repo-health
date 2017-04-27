/*
* issue-stats.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Create issue-stats component.
*/

import template from '../utils/base.template';

const issueStatsComponent = {
  template,
  bindings: {
    issueStatsUrl: '='
  },
  controller: class issueStatsComponent {
    stats = null;
    charts = null;
    loadingStats = true;
    loadingMsg = 'Loading issue stats...';
    numOfStatsSections = 0;

    constructor( $http, $state, StatsService ) {
      'ngInject';
      Object.assign(this, { $http, $state, StatsService });
    }

    $onInit() {
      if (this.issueStatsUrl) {
        this.StatsService.getStatsForUrl(this.issueStatsUrl).then(stats => {
          this.charts = stats.charts;
          this.stats = stats.metrics;
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

export default issueStatsComponent;
