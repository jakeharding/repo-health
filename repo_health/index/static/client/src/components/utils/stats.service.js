/*
* stats.service.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the stats service.
*/

/**
 * Tracks constants for chart names.
 */
const chartNameEnum = {
  dateChart: 'date' // Track date as a chart to tell what metrics are dates
}

class StatsService {

  constructor ( $http, $filter ) {
    'ngInject';
    Object.assign( this, { $http, $filter} )
  }

  /**
  * @description Returns an array of indices to enable iteration over a range in a template
  * @param statsLength
  * @returns {[*]}
  */
  getRangeForSections(statsLength) {
    return [...Array(Math.floor(statsLength / 2)).keys()];
  }

  /**
  * @description Returns the raw data for the metric based on the chart name
  * @param stat
  * @returns {*|string}
  */
  getRawData(stat) {
    let rawData = stat.raw_data;
    if ( stat.is_date ) {
      rawData = this.$filter('date')(rawData);
    }
    return rawData || 'No';
  }

  /**
   * @description Makes a get request to the given url.
   * @param url
   */
  getStatsForUrl (url) {
    return this.$http.get(url).then(stats => {
      let charts = stats.data.charts;
      let metrics = this.$filter('orderBy')(stats.data.metrics, 'ordering');
      return {metrics, charts};
    });
  }
}

export default StatsService;