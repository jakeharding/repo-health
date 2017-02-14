/*
* search.spec.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the test file for the search component
*/

describe('Search', () => {
  beforeEach(module('components.search'));

  describe('SearchController', () => {
    let $componentController;
    let controller;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      controller = $componentController('search');
    }));

    describe('constructor', () => {
      it('should setup the controller', () => {
        expect(controller).toBeDefined;
      });
    });

    describe('getStats', () => {
      it('should return the stats', () => {
        //Add tests when function is implemented
      });
    });
  });
});