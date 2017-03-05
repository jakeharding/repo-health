/*
* repo-details.spec.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the test file for the search component
*/

describe('Repo Details', () => {
  let $rootScope;

  beforeEach(angular.mock.module(
    'app.resources', 
    'components.search', 
    'components.repo-details')
  );

  describe('RepoDetailsController', () => {
    let $componentController;
    let controller;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      $rootScope = $injector.get('$rootScope');
      controller = $componentController('repoDetails');
    }));

    describe('constructor', () => {
      it('should setup the controller', () => {
        expect(controller).toBeDefined;
      });
      
      it('should setup loadingRepo and details', () => {
        expect(controller.loadingRepo).toBeTrue;
        expect(controller.details).toBeNull;
      });

      it('should setup RepoDetailsService, $state, $stateParams', () => {
        expect(controller.RepoDetailsService).toBeOk;
        expect(controller.$state).toBeOk;
        expect(controller.$stateParams).toBeOk;
      });
    });

    describe('getStats', () => {
      it('should make a call to service', async () => {
        spyOn(controller.RepoDetailsService, 'getStats').and.returnValue(Promise.resolve({ name: 'cakephp' }));
        expect(controller.RepoDetailsService.getStats).not.toHaveBeenCalled;
        controller.getStats();
        $rootScope.$apply();
        expect(controller.loadingRepo).toBeFalse;
        expect(controller.details).toBe({ name: 'cakephp' });
        expect(controller.RepoDetailsService.getStats).toHaveBeenCalled;
      });
    });
  });
});