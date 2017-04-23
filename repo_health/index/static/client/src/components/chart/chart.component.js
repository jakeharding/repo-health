/*
* chart.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Create chart component.
*/

import template from './chart.template';

const chartComponent = {
  template,
  bindings: {
    'metric': '=',
    'chart': '='
  },
  controller: class chartComponentController {
    options = null;
    hasData = true;
    titleText = '';
    constructor() {
      'ngInject';
    }

    $onInit() {
      this.titleText = this.chart.title;
      if ( this.metric.raw_data.length === 0) {
        this.hasData = false;
        this.titleText = `No data for the ${this.chart.title} chart to display`;
      }
      this.options = {
        title: {
          display: true,
          text: this.titleText
        }
      }
    }
  }
};

export default chartComponent;
