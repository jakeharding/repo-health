/*
*issue-stats.controller.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* J.Harding
*
* Controller for the issue stats named view.
*
*/

import BaseStatsController from '../base-component/base-stats.controller';

export default class IssueStatsController extends BaseStatsController {

     constructor ($state, issueStatsUrl) {
         super($state, issueStatsUrl);
         Object.assign(this, {$state, issueStatsUrl});
    }
}