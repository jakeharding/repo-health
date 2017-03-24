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

import template from '../base-component/base.template';
import BaseStatsComponent from '../base-component/base-stats.component';

const issueStatsComponent = {
  template,
  bindings: {issueStatsUrl: '='},
  controller: class issueStatsComponent extends BaseStatsComponent {
    stats = null;
    loadingStats = true;
    loadingMsg = "Loading issue stats...";
    numOfStatsSections = 0;


    constructor( $http, $filter ) {
      super($http, $filter);
      'ngInject';
      Object.assign(this, { $http });
    }

    $onInit() {
      if (this.issueStatsUrl) {
        this.getStatsForUrl(this.issueStatsUrl);
        // this.$http.get(this.issueStatsUrl).then(stats => {
        //     this.stats = this.$filter('orderBy')(stats.data.metrics, 'ordering');
        //     this.numOfStatsSections = new Array(Math.floor(this.stats.length / 2)).fill().map((x,i) => {return i});
        //     this.loadingStats = false;
        // });
      }
    }
  }
};

export default issueStatsComponent;
