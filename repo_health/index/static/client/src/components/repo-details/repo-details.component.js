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

/**
 * Tracks constants for chart names.
 */
const chartNameEnum = {
  dateChart: 'date' // Track date as a chart to tell what metrics are dates
}

const repoDetailsComponent = {
  template,
  bindings: {detailsUrl: '='},
  controller: class repoDetailsComponent {

    loadingStats = true;
    loadingMsg = "Loading general repo stats...";
    stats = null;
    numOfStatsSections = 0;

    constructor($http, $filter) {
      'ngInject';
      Object.assign(this, { $http, $filter });
    }

    $onInit() {
      if (this.detailsUrl) {
        this.$http.get(this.detailsUrl).then(details => {
            this.stats = this.$filter('orderBy')(details.data.metrics, 'ordering');
            this.numOfStatsSections = new Array(this.stats.length / 2).fill().map((x,i)=>i);
            this.loadingStats = false;
        });
      }
    }

    getRawDataForChartName(ind) {
      let rawData = this.stats[ind].raw_data;
      switch ( this.stats[ind].chart_name ) {
          case chartNameEnum.dateChart:
            rawData = this.$filter('date')(rawData);
            break;
      }
      return rawData || 'No';
    }
  }
};

export default repoDetailsComponent;
