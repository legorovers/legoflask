angular.module('legorover.main.controller', []).controller('mainController', function ($scope, $location, planService) {
    'use strict';
    $scope.plans = {
        list: planService.get()
    };
    $scope.deletePlan = function (id) {
        planService.remove(id);
    };
    $scope.sendPlans = function () {
        $scope.sendingPlans = true;
        planService.send().then(function () {
            $scope.sendingPlans = false;
        });
    };
});