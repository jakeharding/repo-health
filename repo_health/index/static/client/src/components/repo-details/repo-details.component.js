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

import template from './repo-details';

const repoDetailsComponent = {
  template,
  controller: class repoDetailsComponent {

    loadingRepo = true;
    details = null;

    constructor(RepoDetailsService, $state, $stateParams, $filter) {
      'ngInject';
      Object.assign(this, { RepoDetailsService, $state, $stateParams, $filter });
    }

    $onInit() {
      if (this.hasValidStateParams())
        this.getStats();
    }

    hasValidStateParams () {
      let nulls = this.$filter('filter')(Object.keys(this.$stateParams), (key) => {
        return !!this.$stateParams[key];
      });
      return nulls.length != 0;
    }

    getStats() {
      this.RepoDetailsService.getStats(this.$stateParams).then(details => {
        this.loadingRepo = false;
        this.details = details;
      }, () => this.$state.go('search'));
    }
  }
};

export default repoDetailsComponent;
