/*
* karma-test-runner.js - (C) Copyright - 2017
* This software is copyrighted to contributors listed in CONTRIBUTIONS.md.
*
* SPDX-License-Identifier: MIT
*
* Author(s) of this file:
* @bparish628
*
* This is the entry point for all of our tests.
*/

import 'angular';
import 'angular-mocks';

import 'main.module';

var context = require.context('./src', true, /\.spec\.js?$/);
context.keys().forEach(context);