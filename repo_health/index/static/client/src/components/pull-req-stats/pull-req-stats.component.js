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

    labels = ['Jan', 'feb', 'Mar', 'April', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    series = ['Series A', 'Series B'];
    data = [
      [65, 59, 80, 81, 56, 55, 40],
      [28, 48, 40, 19, 86, 27, 90]
    ];
    onClick = function (points, evt) {
      console.log(points, evt);
    };
    onHover = function (points) {
      if (points.length > 0) {
        console.log('Point', points[0].value);
      } else {
        console.log('No point');
      }
    };
    datasetOverride = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];

    options = {
      scales: {
        yAxes: [
          {
            id: 'y-axis-1',
            type: 'linear',
            display: true,
            position: 'left'
          },
          {
            id: 'y-axis-2',
            type: 'linear',
            display: true,
            position: 'right'
          }
        ]
      }
    };
    
    constructor( $http, $filter ) {
      super($filter);
      'ngInject';
      Object.assign(this, { $http });
    }

    $onInit() {
      if (this.prStatsUrl) {
        this.$http.get(this.prStatsUrl).then(stats => {
            this.stats = this.$filter('orderBy')(stats.data.metrics, 'ordering');
            this.numOfStatsSections = new Array(Math.floor(this.stats.length / 2)).fill().map((x,i) => {return i});
            this.loadingStats = false;
        });
      }
    }
  }
};

export default pullReqStatsComponent;
