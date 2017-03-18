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

import template from './search';

const searchComponent = {
  template,
  controller: class searchComponent {

    loadingRepo = false;
    error = null;

    constructor(RepoDetailsService, $state, $stateParams) {
      'ngInject';
      Object.assign(this, { RepoDetailsService, $state, $stateParams });
    }

    getStats() {
      const params = this.RepoDetailsService.getNameAndOwnerFromUrl(this.githubUrl);
      if (params) {
        this.loadingRepo = true;
        this.error = null;
        this.RepoDetailsService.getStats(params).then(() => {
          this.$state.go('repo-details', params);
        }, () => {
          this.error = 'This repo does not exist';
          this.loadingRepo = false;
        });
      }
    }
  }
};

export default searchComponent;
