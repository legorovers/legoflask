angular.module('legorover.trigger.service', []).factory('triggerService', function () {
    'use strict';
    function get() {
        return [
            {
                title: 'obstacle'
            },
            {
                title: 'hole'
            },
            {
                title: 'explosion'
            }
        ];
    }
    return {
        get: get
    };
});