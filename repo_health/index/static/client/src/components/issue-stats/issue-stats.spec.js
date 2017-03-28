/*
* issue-stats.spec.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the test file for the issue stats component
*/

const module = angular.mock.module;

describe('Issue Stats', () => {

  beforeEach(module(
    'repo-health',
    'components.issue-stats'
  ), ($provide) => {
    $provide.provider('StatsService', () => {
      return {
        then: () => {
          return "Mock";
        }
      };
    })
  });

  describe('IssueStatsComponent', () => {
    let $componentController, $httpBackend, $apiUrl;
    let controller, getIssueStatsUrl;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      $httpBackend = $injector.get('$httpBackend');
      $apiUrl = $injector.get('$apiUrl');
      getIssueStatsUrl = `${$apiUrl}/${jasmine.any(Number)}/issues`;
      controller = $componentController('issueStats', null, {issueStatsUrl: getIssueStatsUrl});
      $httpBackend.when('GET', getIssueStatsUrl).respond(200, {metrics: [{
          ordering: 1
      }]});
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
            $httpBackend.expectGET(getIssueStatsUrl)
            controller.$onInit();
            $httpBackend.flush();
        })
    });
  });
});