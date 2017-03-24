/*
* base-stats.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the base controller for the components to hold some commone methods.
*/

/**
 * Tracks constants for chart names.
 */
const chartNameEnum = {
  dateChart: 'date' // Track date as a chart to tell what metrics are dates
}

export default class BaseStatsComponent {

    constructor ( $http, $filter ) {
        Object.assign( this, { $http, $filter} )
    }
    /**
    * @description Returns the raw data for the metric based on the chart name
    * @param ind
    * @returns {*|string}
    */
    getRawDataForChartName(ind) {
      let rawData = this.stats[ind].raw_data;
      switch ( this.stats[ind].chart_name ) {
          case chartNameEnum.dateChart:
            rawData = this.$filter('date')(rawData);
            break;
      }
      return rawData || 'No';
    }

    getStatsForUrl (url) {
        this.$http.get(url).then(stats => {
            this.stats = this.$filter('orderBy')(stats.data.metrics, 'ordering');
            this.numOfStatsSections = new Array(Math.floor(this.stats.length / 2)).fill().map((x,i) => {return i});
            this.loadingStats = false;
        });
    }
}