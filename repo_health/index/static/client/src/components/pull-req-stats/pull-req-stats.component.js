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
import BaseStatsComponent from '../base-component/base-stats.component';

const pullReqStatsComponent = {
  template,
  bindings: {prStatsUrl: '='},
  controller: class pullReqStatsComponent extends BaseStatsComponent {
    stats = null;
    loadingStats = true;
    loadingMsg = "Loading pull request stats...";
    numOfStatsSections = 0;
    
    constructor( $http, $filter ) {
      super($http, $filter);
      'ngInject';
      Object.assign(this, { $http });
    }

    $onInit() {
      if (this.prStatsUrl) {
          this.getStatsForUrl(this.prStatsUrl);
      }
    }
  }
};

export default pullReqStatsComponent;
