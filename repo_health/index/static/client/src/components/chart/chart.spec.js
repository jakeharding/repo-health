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
    const mockMetricEmptyData = {
      raw_data: []
    };
    const mockChart = {
      title: "Fake title"
    };

    beforeEach(inject($injector => {
      $componentController = $injector.get('$componentController');
      controller = $componentController('chart', null, {
        metric: mockMetricEmptyData,
        chart: mockChart
      });
    }));

    describe('constructor', () => {
      it('should setup the controller with a chart and metric property', () => {
        expect(controller.chart).toBe(mockChart);
        expect(controller.metric).toBe(mockMetricEmptyData);
      });

      it('should set the title text in the onInit method', () => {
        controller.$onInit();
        expect(controller.titleText).toBe(`No data for the ${mockChart.title} chart to display`)
      })
    })
  })
})