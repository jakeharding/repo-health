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

const module = angular.mock.module;

describe('Search', () => {
  let sandbox;

  beforeEach(module(
    'app.resources',
    'repo-health',
    'components.repo-details',
    'components.pull-req-stats',
    'components.search'
  ));

  describe('SearchController', () => {
    let $componentController;
    let $rootScope;
    let RepoDetailsService;
    let $q;
    let controller;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      $rootScope = $injector.get('$rootScope');
      $q = $injector.get('$q');
      RepoDetailsService = $injector.get('RepoDetailsService');
      controller = $componentController('search');
    }));

    describe('constructor', () => {
      it('should setup the controller', () => {
        expect(controller).toBeDefined();
      });
      it('should setup loadingRepo and error', () => {
        expect(controller.error).toBeNull();
      });
    });

    describe('getStatsUrls', () => {

      it('should not make a call if url is invalid', () => {
        spyOn(controller.$state, 'go');
        controller.githubUrl = 'This not a url';
        controller.getStatsUrls();
        expect(controller.error).toBeTruthy();
        expect(controller.$state.go).not.toHaveBeenCalledWith('repo-health');
      });

      it('should make a call to getStatsUrls on the service', () => {
        spyOn(controller.RepoDetailsService, 'getStatsUrls').and.returnValue($q.resolve({ name: 'cakephp' }));
        controller.githubUrl = 'https://github.com/cakephp/cakephp';
        controller.getStatsUrls();
        expect(controller.RepoDetailsService.getStatsUrls).toHaveBeenCalled();
      });

      it('should set an error if it fails', () => {
        controller.githubUrl = 'https://github.com/cakephp/';
        controller.getStatsUrls();
        $rootScope.$apply();
        expect(controller.error).toBeTruthy();
      });
    });
  });
});