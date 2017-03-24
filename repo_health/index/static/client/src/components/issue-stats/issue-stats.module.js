/*
* issue-stats..module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Definition for the issue stats module
*/

import issueStatsComponent from './issue-stats.component';

const components = angular
  .module('components.issue-stats', [])
    .component('issueStats', issueStatsComponent)
  .name;

export default components;