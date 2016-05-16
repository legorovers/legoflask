angular.module('legorover.trigger.service', []).factory('triggerService', function () {
    'use strict';
    function get() {
        return [
            {
                title: 'collision'
            },
            {
                title: 'dark ground'
            },
            {
                title: 'noise'
            }
        ];
    }
    return {
        get: get
    };
});