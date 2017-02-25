/*
* component.module.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the definitions for all of the components used in this application.
*/

import search from './search/search.module';

const components = angular
  .module('components', [
    search
  ])
  .name;

export default components;