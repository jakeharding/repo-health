/*
* stats.service.js - (C) Copyright - 2017
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

class StatsService {

    constructor ( $http, $filter ) {
      Object.assign( this, { $http, $filter} )
    }

    getRangeForSections(statsLength) {
      return [...Array(Math.floor(statsLength / 2)).keys()];
    }

    /**
    * @description Returns the raw data for the metric based on the chart name
    * @param index
    * @returns {*|string}
    */
    getRawDataForChartName(index) {
      let rawData = this.stats[index].raw_data;
      switch ( this.stats[index].chart_name ) {
        case chartNameEnum.dateChart:
          rawData = this.$filter('date')(rawData);
          break;
      }
      return rawData || 'No';
    }

  /**
   * @description Makes a get request to the given url.
   * @param url
   */
  getStatsForUrl (url) {
    return this.$http.get(url).then(stats => {
      stats = this.$filter('orderBy')(stats.data.metrics, 'ordering');
      return stats;
    });
  }
}

export default StatsService;