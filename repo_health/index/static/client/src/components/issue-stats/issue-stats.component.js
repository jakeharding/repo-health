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
  controller: class issueStatsComponent {
    stats = null;
    loadingStats = true;
    loadingMsg = "Loading issue stats...";
    numOfStatsSections = 0;


    constructor( $http, $state ) {
      'ngInject';
      Object.assign(this, { $http, $state });
    }

    $onInit() {
      if (this.issueStatsUrl) {
        // TODO Write service to make API request for stats.
        // this.getStatsForUrl(this.issueStatsUrl);
      } else {
        this.$state.go('search', {
          error: true
        });
      }
    }
  }
};

export default issueStatsComponent;
