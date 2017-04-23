/*
* stats.service.spec.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the test file for the stats service.
*/

const module = angular.mock.module;

describe("StatsService", () => {
  let StatsService, $httpBackend, $q;
  let someFakeUrl = 'some/fake/url';
  beforeEach(module(
    'repo-health'
  ));

  beforeEach(inject(($injector) => {
    StatsService = $injector.get('StatsService');
    $httpBackend = $injector.get('$httpBackend');
    $q = $injector.get('$q');
  }));

  describe('getStatsForUrl', () => {
    beforeEach(() => {
      $httpBackend.when('GET', someFakeUrl).respond(200, {
        metrics: [],
        charts: {}
      });
    });
    afterEach(() => {
      $httpBackend.verifyNoOutstandingExpectation();
      $httpBackend.verifyNoOutstandingRequest();
    });

    it('should make a request to the given url', () => {
      $httpBackend.expectGET(someFakeUrl);
      let result = StatsService.getStatsForUrl(someFakeUrl);
      $httpBackend.flush();
      result.then(res => {
        expect(res.charts).toBeDefined();
        expect(res.metrics).toBeDefined();
      })
    });
  })

  describe('getStatsSections', () => {
    it('should return an array the floor of half the size input', () => {
      let range = StatsService.getRangeForSections(9);
      expect(Array.isArray(range)).toBeTruthy();
      expect(range.length).toBe(4);
    });
  });

  describe('getRawDataForChartName', () => {
    it('should call the $filter if chart name is `date`', () => {
      spyOn(StatsService, '$filter').and.callThrough();
      let mockStat = {
        chart_name: 'date',
        raw_data: "2013-10-05T11:40:36"// Must have a valid date format for $filter to use it
      }
      expect(StatsService.getRawDataForChartName(mockStat)).not.toBe(mockStat.raw_data);
      expect(StatsService.$filter).toHaveBeenCalledWith('date');
    });

    it('should the raw data is the chart name is null', () => {
      let mockStat = {
        raw_data: 89,
        chart_name: null
      }
      expect(StatsService.getRawDataForChartName(mockStat)).toBe(mockStat.raw_data);
    });

    it('should return `No` is the raw_data is 0', () => {
      let mockStat = {
        raw_data: 0
      }
      expect(StatsService.getRawDataForChartName(mockStat)).toBe('No');
    })
  })
});