angular.module('legorover.action.service', []).factory('actionService', function () {
    'use strict';
    function get() {
        return [
            {
                title: 'left'
            },
            {
                title: 'right'
            },
            {
                title: 'forward'
            },
            {
                title: 'back'
            },
            {
                title: "stop"
            }
        ];
    }
    return {
        get: get
    };
});