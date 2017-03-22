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
    let $componentController, $httpBackend, $apiUrl;
    let controller, getPrStatsUrl;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      $httpBackend = $injector.get('$httpBackend');
      $apiUrl = $injector.get('$apiUrl');
      getPrStatsUrl = `${$apiUrl}/${jasmine.any(Number)}/pull-requests`;
      controller = $componentController('pullReqStats', null, {prStatsUrl: getPrStatsUrl});
      $httpBackend.when('GET', getPrStatsUrl).respond(200, {some: 'cakephp', data: 15});

    }));

    afterEach(() => {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe('constructor', () => {

        it('should setup the controller', () => {
            expect(controller).toBeDefined();
        });

        it('should make a request to get the stats in the $onInit method', () => {
            $httpBackend.expectGET(getPrStatsUrl)
            controller.$onInit();
            $httpBackend.flush();
        })
    });
  });
});