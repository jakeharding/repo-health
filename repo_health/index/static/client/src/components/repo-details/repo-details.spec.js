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
    let $httpBackend;
    let $apiUrl, getStatsReqUrl, getDetailsUrl;

    beforeEach(module(
        'app.resources',
        'components.search',
        'components.repo-details',
    ));
    beforeEach(inject(($injector) => {
        $httpBackend = $injector.get("$httpBackend");
        $apiUrl = $injector.get('$apiUrl');
        getStatsReqUrl = `${$apiUrl}?name=cakephp&owner__login=cakephp`;
        getDetailsUrl = `${$apiUrl}/${jasmine.any(Number)}`;

    }));

    afterEach(() => {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe('RepoDetailsController', () => {
        let $componentController;
        let controller;

        beforeEach(inject(($injector) => {
            $componentController = $injector.get('$componentController');
            controller = $componentController('repoDetails', null, { detailsUrl: getDetailsUrl, stats: []});
            $httpBackend.when('GET', getDetailsUrl).respond(200, {
                metrics: [{
                    ordering: 1
                },{
                    ordering: 2
                }]
            });
        }));

        describe('constructor', () => {
            it('should setup the controller', () => {
                expect(controller).toBeDefined();
                expect(controller.loadingStats).toBeTruthy();
            });

            it('should request the details in the $onInit method', () => {
                $httpBackend.expectGET(getDetailsUrl);
                controller.$onInit();
                $httpBackend.flush();
            });
        });
    });

    describe('RepoDetailsService', () => {
        let RepoDetailsService;

        beforeEach(inject(($injector) => {
            RepoDetailsService = $injector.get('RepoDetailsService');
        }));

        describe('getNameAndOwnerFromUrl', () => {
            it('should return name and owner', () => {
                expect(RepoDetailsService.getNameAndOwnerFromUrl('https://github.com/name/repo')).toEqual({
                    name: 'repo',
                    owner__login: 'name'
                });
            });

            it('should return undefined', () => {
                expect(RepoDetailsService.getNameAndOwnerFromUrl()).toBeUndefined();
                expect(RepoDetailsService.getNameAndOwnerFromUrl('not a url')).toBeUndefined();
                expect(RepoDetailsService.getNameAndOwnerFromUrl('https://github.com/name')).toBeUndefined();
            });
        });

        describe('getStatsUrls', () => {
            beforeEach(() => {
                $httpBackend.when('GET', getStatsReqUrl).respond(200, {repo_details_url: 'cakephp', pr_stats_url: 15});
            });

            it('should make a request to get the urls', () => {
                $httpBackend.expectGET(getStatsReqUrl);
                RepoDetailsService.getStatsUrls({name: 'cakephp', owner__login: 'cakephp'});
                $httpBackend.flush();

            });
        });
    });
});