/*
* search.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the creation of the search component.
*/

import template from '../base-component/base.template';

const repoDetailsComponent = {
  template,
  bindings: {detailsUrl: '='},
  controller: class repoDetailsComponent {

    loadingStats = true;
    loadingMsg = "Loading general repo stats...";
    stats = null;

    constructor($http) {
      'ngInject';
      Object.assign(this, { $http });
    }

    $onInit() {
      this.$http.get(this.detailsUrl).then(details => {
        this.stats = details.data;
        this.loadingStats = false;
      });
    }
  }
};

export default repoDetailsComponent;
