/*
* search.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the creation of the search component.
*/

import template from '../utils/base.template';

const repoDetailsComponent = {
  template,
  bindings: {
    detailsUrl: '='
  },
  controller: class repoDetailsComponent {

    loadingStats = true;
    loadingMsg = "Loading general repo stats...";
    stats = null;
    charts = null;
    numOfStatsSections = 0;

    constructor($http, StatsService, $state) {
      'ngInject';
      Object.assign(this, { $http, StatsService, $state });
    }

    $onInit() {
      if (this.detailsUrl) {
        this.StatsService.getStatsForUrl(this.detailsUrl).then(stats => {
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

export default repoDetailsComponent;
