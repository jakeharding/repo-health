/*
* pull-req-stats.module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the module definition for the pr stats module
*/

import pullReqStatsComponent from './pull-req-stats.component';

const components = angular
  .module('components.pull-req-stats', [])
  .component('pullReqStats', pullReqStatsComponent)
  .name;

export default components;