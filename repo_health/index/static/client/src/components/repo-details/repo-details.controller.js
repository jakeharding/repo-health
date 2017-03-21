/*
*repo-details.controller.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Extend base stats controller to handle error state.
* Adds the ability to inject the specific resolve of the details url.
*
*/

import BaseStatsController from '../base-component/base-stats.controller';

export default class RepoDetailsController extends BaseStatsController {

     constructor ($state, detailsUrl) {
         super($state, detailsUrl);
         Object.assign(this, {$state, detailsUrl});
    }
}