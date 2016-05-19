angular.module('legorover.action.service', []).factory('actionService', function () {
    'use strict';
    function get() {
        return [
            {
                title: 'forward'
            },
            {
                title: 'left'
            },
            {
                title: 'right'
            },
            {
                title: 'back'
            },
            {
                title: "stop"
            },
            {
                title: "turn-left"
            },
            {
                title: "turn-right"
            },
            {
                title: "speak"
            }
        ];
    }
    return {
        get: get
    };
});