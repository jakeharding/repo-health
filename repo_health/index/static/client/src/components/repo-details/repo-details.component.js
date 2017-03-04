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

    constructor(RepoDetailsService, $state, $stateParams) {
      'ngInject';
      Object.assign(this, { RepoDetailsService, $state, $stateParams });
    }

    $onInit() {
      this.getStats();
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
