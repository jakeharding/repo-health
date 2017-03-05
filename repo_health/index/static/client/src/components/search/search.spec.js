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
  beforeEach(angular.mock.module(
    'app.resources', 
    'components.search', 
    'components.repo-details')
  );

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
      it('should setup loadingRepo and error', () => {
        expect(controller.loadingRepo).toBeFalse;
        expect(controller.error).toBeNull;
      });
    });

    describe('getStats', () => {
      beforeEach(() => {
        spyOn(controller.RepoDetailsService, 'getStats').and.returnValue(Promise.resolve({ name: 'cakephp' }));
      });

      it('should not make a call if url is invalid', () => {
        controller.githubUrl = 'This not a url';
        controller.getStats();
        expect(controller.loadingRepo).toBeTrue;
        expect(controller.RepoDetailsService.getStats).not.toHaveBeenCalled;
      });

      it('should make a call to getStats on the service', async () => {
        controller.githubUrl = 'https://github.com/cakephp/cakephp';
        controller.getStats();
        expect(controller.loadingRepo).toBeTrue;
        expect(controller.RepoDetailsService.getStats).toHaveBeenCalled;
      });

      it('should set an error if it fails', async () => {
        spyOn(controller.RepoDetailsService, 'getStats').and.returnValue(Promise.reject('error'));
        controller.githubUrl = 'https://github.com/cakephp/cakephp';
        controller.getStats();
        expect(controller.loadingRepo).toBeFalse;
        expect(controller.error).toBe('This repo does not exist');
        expect(controller.RepoDetailsService.getStats).toHaveBeenCalled;
      });
    });
  });
});