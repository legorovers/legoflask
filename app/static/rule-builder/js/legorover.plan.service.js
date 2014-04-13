angular.module('legorover.plan.service', []).factory('planService', function ($http) {
    'use strict';
    var plans = [];
    function send() {
        return $http.post('/api/rules/', plans);
    }
    function get(id) {
        var i, len;
        if (id) {
            for (i = 0, len = plans.length; i < len; i += 1) {
                if (plans[i].id === parseInt(id)) {
                    return plans[i];
                }
            }
            return;
        }
        return plans;
    }
    function create() {
        var id = 1,
            newPlan = {
                title: 'New plan',
                trigger: '',
                actions: [],
                active: true
            };
        do {
            id += 1;
        } while (get(id));
        newPlan.id = id;
        plans.push(newPlan);
        return plans[plans.length - 1];
    }
    function remove(id) {
        var plan, position;
        plan = get(id);
        if (plan) {
            position = plans.indexOf(plan);
            if (position > -1) {
                plans.splice(position, 1);
                return plan;
            }
        }
        return;
    }
    return {
        get: get,
        create: create,
        remove: remove,
        send: send
    };
});