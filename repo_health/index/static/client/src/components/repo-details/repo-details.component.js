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

import template from '../base-component/base.template';
import BaseStatsComponent from '../base-component/base-stats.component';

const repoDetailsComponent = {
  template,
  bindings: {detailsUrl: '='},
  controller: class repoDetailsComponent extends BaseStatsComponent {

    loadingStats = true;
    loadingMsg = "Loading general repo stats...";
    stats = null;
    numOfStatsSections = 0;

    constructor($http, $filter) {
      super($http, $filter );
      'ngInject';
      Object.assign(this, { $http });
    }

    $onInit() {
      if (this.detailsUrl) {
        this.getStatsForUrl(this.detailsUrl);
      }
    }
  }
};

export default repoDetailsComponent;
