/*
* base-stats.controller.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Base stats controller to handle an error state if no repos are returned for an owner login and name request
*/


export default class BaseStatsController {

    constructor ($state, Urls) {
        if (!Urls) {
            $state.go('search', {error:true});
        }
    }
}
