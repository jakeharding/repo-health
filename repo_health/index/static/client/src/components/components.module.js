/*
* component.module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
* J.Harding
*
* This is the definitions for all of the components used in this application.
*/

import search from './search/search.module';
import repoDetails from './repo-details/repo-details.module';
import pullReqStats from './pull-req-stats/pull-req-stats.module';

const components = angular
  .module('components', [
    search,
    repoDetails,
    pullReqStats
  ])
  .name;

export default components;