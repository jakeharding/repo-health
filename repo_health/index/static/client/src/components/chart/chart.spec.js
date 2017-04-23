/*
* chart.spec.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* This is the test file for the chart component
*/

const module = angular.mock.module;

describe('Chart', () => {
  beforeEach(module(
    'repo-health',
    'components.chart'
  ));

  describe('ChartComponent', () => {
    let $componentController, controller;
    const mockMetric = "mock metric";
    const mockChart = "mock chart";

    beforeEach(inject($injector => {
      $componentController = $injector.get('$componentController');
      controller = $componentController('chart', null, {
        metric: mockMetric,
        chart: mockChart
      });
    }));

    describe('constructor', () => {
      it('should setup the controller with a chart and metric property', () => {
        expect(controller.chart).toBe(mockChart);
        expect(controller.metric).toBe(mockMetric);
      })
    })
  })
})