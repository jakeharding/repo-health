/*
*pull-req-stats.controller.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Controller for the pr stats named view.
*
*/

import BaseStatsController from '../base-component/base-stats.controller';

export default class PrStatsController extends BaseStatsController {

     constructor ($state, prStatsUrl) {
         super($state, prStatsUrl);
         Object.assign(this, {$state, prStatsUrl});
    }
}
