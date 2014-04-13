angular.module('legorover.routes', ['ngRoute']).config(['$routeProvider',
    function($routeProvider) {
        'use strict';
        $routeProvider.
            when('/', {
                templateUrl: 'templates/legorover.main.template.html',
                controller: 'mainController'
            }).
            when('/plans/new', {
                templateUrl: 'templates/legorover.plan.template.html',
                controller: 'planController'
            }).
            when('/plans/edit/:planID', {
                templateUrl: 'templates/legorover.plan.template.html',
                controller: 'planController'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);