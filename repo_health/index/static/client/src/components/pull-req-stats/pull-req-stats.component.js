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

import template from './pull-req-stats';

const pullReqStatsComponent = {
  template,
  controller: class pullReqStatsComponent {

    constructor($state, $stateParams) {
      'ngInject';
      Object.assign(this, {  $state, $stateParams });
    }

    $onInit() {
      console.log(this.$stateParams);
    }
  }
};

export default pullReqStatsComponent;
