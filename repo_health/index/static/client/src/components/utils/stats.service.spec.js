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

describe("StatsService", () => {
  let StatsService, $httpBackend;
  let someFakeUrl = 'some/fake/url';
  beforeEach(module(
    'repo-health'
  ));

  beforeEach(inject(($injector) => {
    StatsService = $injector.get('StatsService');
    $httpBackend = $injector.get('$httpBackend');
  }));

  afterEach(() => {
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });

  describe('getStatsForUrl', () => {
    beforeEach(() => {
      $httpBackend.when('GET', someFakeUrl).respond(200, {
        metrics: []
      });
    });
    it('should make a request to the given url', () => {
      $httpBackend.expectGET(someFakeUrl);
      StatsService.getStatsForUrl(someFakeUrl);
      $httpBackend.flush();
    })
  })
})