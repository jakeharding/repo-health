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
  <div layout="row" layout-align="center center">
    <div ui-view flex="65">
      <md-tabs class="repo-tabs" md-dynamic-height md-border-bottom>
        <md-tab label="Details">
          <div ui-view="repo-details"></div>
        </md-tab>
        <md-tab label="Pull Request Stats">
          <div ui-view="pull-req-stats"></div>
        </md-tab>
        <md-tab label="Issue Stats">
          <div ui-view="issue-stats"></div>
        </md-tab>
      </md-tabs>
    </div>
  </div>
`;

const mainComponent = {
  template
};

export default mainComponent;
