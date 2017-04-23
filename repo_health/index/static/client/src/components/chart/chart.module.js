/*
* chart..module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Definition for the chart module
*/

import chartComponent from './chart.component';

const components = angular
  .module('components.chart', [])
    .component('chart', chartComponent)
  .name;

export default components;