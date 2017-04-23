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
    constructor () {
      'ngInject';
    }
  }
};

export default chartComponent;
