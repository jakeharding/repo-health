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

const module = angular.mock.module;

describe('Repo Details', () => {
  let $rootScope;
  let $q;

  beforeEach(module(
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
      $q = $injector.get('$q');
      controller = $componentController('repoDetails');
    }));

    describe('constructor', () => {
      it('should setup the controller', () => {
        expect(controller).toBeDefined();
      });
      
      it('should setup loadingRepo and details', () => {
        expect(controller.loadingStats).toBeTruthy();
        expect(controller.stats).toBeNull();
      });

      // it('should setup RepoDetailsService, $state, $stateParams', () => {
      //   expect(controller.RepoDetailsService).toBeDefined();
      //   expect(controller.$state).toBeDefined();
      //   expect(controller.$stateParams).toBeDefined();
      // });
    });

    // describe('getStatsUrls', () => {
    //   it('should make a call to service', () => {
    //     spyOn(controller.RepoDetailsService, 'getStatsUrls').and.returnValue($q.resolve({ name: 'cakephp' }));
    //     expect(controller.RepoDetailsService.getStatsUrls).not.toHaveBeenCalled();
    //     controller.getStatsUrls();
    //     $rootScope.$apply();
    //     expect(controller.loadingRepo).toBeFalsy();
    //     expect(controller.details).toEqual({ name: 'cakephp' });
    //     expect(controller.RepoDetailsService.getStats).toHaveBeenCalled();
    //   });
    // });
  });

  describe('RepoDetailsService', () => {
    let RepoDetailsService;
    let $httpBackend;
    let $apiUrl;

    beforeEach(inject(($injector) => {
      $rootScope = $injector.get('$rootScope');
      $q = $injector.get('$q');
      $httpBackend = $injector.get('$httpBackend');
      $apiUrl = $injector.get('$apiUrl');
      RepoDetailsService = $injector.get('RepoDetailsService');
    }));

    describe('getNameAndOwnerFromUrl', () => {
      it('should return name and owner', () => {
        expect(RepoDetailsService.getNameAndOwnerFromUrl('https://github.com/name/repo')).toEqual({ name: 'repo', owner__login: 'name' });
      });
      
      it('should return undefined', () => {
        expect(RepoDetailsService.getNameAndOwnerFromUrl()).toBeUndefined();
        expect(RepoDetailsService.getNameAndOwnerFromUrl('not a url')).toBeUndefined();
        expect(RepoDetailsService.getNameAndOwnerFromUrl('https://github.com/name')).toBeUndefined();
      });
    });

    describe('getStatsUrls', () => {
      it('should return a promise if repoDetails exists', () => {
        RepoDetailsService.repoDetails = { name: 'cakephp', watchers: 123 };
        RepoDetailsService.getStats().then(details => {
          expect(details).toEqual(RepoDetailsService.repoDetails);
        });
        $rootScope.$apply();
      });

      it('should set repoDetails if it doesn\'t exist', () => {
        $httpBackend.when('GET', `${$apiUrl}?name=cakephp&owner__login=cakephp`).respond(200, { name: 'cakephp', watchers: 15 });
        RepoDetailsService.getStats({ name: 'cakephp', owner__login: 'cakephp' }).then(details => {
          expect(details).toEqual(RepoDetailsService.repoDetails);
        });
        $httpBackend.flush();
        $rootScope.$apply();
        expect(RepoDetailsService.repoDetails.name).toEqual('cakephp');
        expect(RepoDetailsService.repoDetails.watchers).toEqual(15);
      });
    });
  });
});