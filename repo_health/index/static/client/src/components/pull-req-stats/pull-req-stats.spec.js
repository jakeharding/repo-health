/*
* pull-req-stats.spec.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the test file for the search component
*/

const module = angular.mock.module;

describe('Pull Req Stats', () => {

  beforeEach(module(
    'app.resources',
    'components.search',
    'components.repo-details',
    'components.pull-req-stats'
  ));

  describe('PullReqStatsController', () => {
    let $componentController;
    let controller;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      controller = $componentController('pullReqStats');
    }));

    describe('constructor', () => {
        it('should setup the controller', () => {
            expect(controller).toBeDefined();
        });
    });

  });
});