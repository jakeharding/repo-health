/*
* main.component.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the creation of the search component.
*/

const template = `
  <div layout="row" layout-align="center center">
    <h1 class="md-display-3 text-center">Repo Health Assessment</h1>
  </div>
  <div layout="row">
    <div ui-view flex>
      <div ui-view="repo-details"></div>
      <div ui-view="pull-req-stats"></div>
    </div>
  </div>
`;

const mainComponent = {
  template
};

export default mainComponent;
