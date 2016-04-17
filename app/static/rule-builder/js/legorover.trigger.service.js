angular.module('legorover.trigger.service', []).factory('triggerService', function () {
    'use strict';
    function get() {
        return [
            {
                title: 'left obstacle'
            },
            {
                title: 'right obstacle'
            },
            {
                title: 'proximity'
            }
        ];
    }
    return {
        get: get
    };
});