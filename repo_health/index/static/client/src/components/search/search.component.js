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

    error = null;
    errorMsg = 'This repo does not exist';

    constructor(RepoDetailsService, $state, $stateParams) {
      'ngInject';
      Object.assign(this, { RepoDetailsService, $state, $stateParams });
      this.error = $stateParams.error;
    }

    getStatsUrls() {
        const params = this.RepoDetailsService.getNameAndOwnerFromUrl(this.githubUrl);
        if (params) {
            this.error = null;
            this.$state.go('repo-health', params);
        } else  {
            this.error = true;
        }
    }
  }
};

export default searchComponent;
