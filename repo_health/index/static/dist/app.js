
(function () {
    angular.module('app', ['ui.router'])

        .config(function($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('');
            $stateProvider.state('home', {
                templateUrl: 'static/dist/home.html',
                url: '',
                controller: 'HomeCtrl',
                controllerAs: 'vm'
            })
        })
})();