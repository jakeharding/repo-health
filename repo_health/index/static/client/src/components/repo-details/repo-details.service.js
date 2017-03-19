/*
* repo-details.service.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the module definition for the repo-details service
*/

class RepoDetailsService {

  repoDetails = null;

  constructor ($repo, $q){
    'ngInject';

    Object.assign(this, { $repo, $q });
  }

  /* Gets the last two strings on a url */
  getNameAndOwnerFromUrl(url = '') {
    // if (url.search('github.com') == -1) {
    //   return;
    // }

    const pathArray = url.replace(/.*github.com\//, '').split('/');
    const name = pathArray.pop();
    const owner__login = pathArray.pop();
    return name && owner__login ? { owner__login, name } : undefined;
  }

  getStats(params) {
    // if (this.repoDetails) {
    //   return this.$q.resolve(this.repoDetails);
    // } else {
    return this.$repo.get('repo', params).then(details => (this.repoDetails = details));
    // }
  }

}

export default RepoDetailsService;