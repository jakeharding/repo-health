import ngResource from 'angular-resource';

const resources = angular.module('app.resources', [ ngResource ])
  .value('$apiUrl', '/api/v1/gh-projects')

  .factory('$api', function($resource, $apiUrl) {
    'ngInject';

    const idAndVerb = {
      id: '@id',
      verb: '@verb'
    };

    const api = {
      idAndVerb,

      add(config) {
        var params;
        var url;

        const orig = angular.copy(idAndVerb);
        params = angular.extend(orig, config.params);
        url = $apiUrl + config.url + '/:id/:verb';

        api[config.resource] = $resource(url, params);
      }
    };

    return api;
  })

  .provider('$repo', {

    list(resource, query){ 
      return $repo => $repo.list(resource, query);
    },

    get(resource) { 
      return $repo => $repo.get(resource);
    },

    $get($q, $api) {

      const repo = {

        list(resource, query) {
          let queryObject = {};

          if (angular.isObject(query)) {
            queryObject = angular.extend(queryObject, query);
          }

          return $api[resource].query(queryObject).$promise;
        },

        get(resource, params) {
          return $api[resource].get(params).$promise;
        }
      };

      return repo;
    }
  })
  .name;

export default resources;
