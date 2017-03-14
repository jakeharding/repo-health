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
    'components.repo-details',
    'components.search')
  );

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
        expect(controller.loadingRepo).toBeFalsy();
        expect(controller.error).toBeNull();
      });
    });

    describe('getStats', () => {
      let getStats;

      it('should not make a call if url is invalid', () => {
        spyOn(controller.RepoDetailsService, 'getStats');
        controller.githubUrl = 'This not a url';
        controller.getStats();
        expect(controller.loadingRepo).toBeTrue;
        expect(controller.RepoDetailsService.getStats).not.toHaveBeenCalled();
      });

      it('should make a call to getStats on the service', () => {
        spyOn(controller.RepoDetailsService, 'getStats').and.returnValue($q.resolve({ name: 'cakephp' }));
        controller.githubUrl = 'https://github.com/cakephp/cakephp';
        controller.getStats();
        expect(controller.loadingRepo).toBeTruthy();
        expect(controller.RepoDetailsService.getStats).toHaveBeenCalled();
      });

      it('should set an error if it fails', () => {
        spyOn(controller.RepoDetailsService, 'getStats').and.returnValue($q.reject('error'));
        controller.githubUrl = 'https://github.com/cakephp/cakephp';
        controller.getStats();
        $rootScope.$apply();
        expect(controller.loadingRepo).toBeFalsy();
        expect(controller.error).toEqual('This repo does not exist');
        expect(controller.RepoDetailsService.getStats).toHaveBeenCalled();
      });
    });
  });
});