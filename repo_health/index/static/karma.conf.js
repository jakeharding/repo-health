const webpack = require('webpack');
const webpackConfig = require('./webpack.config');

const testWebpackConfig = Object.assign({}, webpackConfig, {
 watch: true,
 plugins: [
   new webpack.ProvidePlugin({
     $: 'jquery',
     jQuery: 'jquery',
     'window.jQuery': 'jquery'
   })
 ]
});

module.exports = (config) => {
  config.set({
    basePath: '',
    frameworks: ['jasmine'],
    webpack: testWebpackConfig,
    webpackMiddleware: {
      noInfo: true
    },
    files: [
      './client/karma-test-runner.js',
    ],
    exclude: [
    ],
    plugins: [
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-webpack')
    ],
    preprocessors: {
      './client/karma-test-runner.js': ['webpack']
    },
    reporters: ['progress'],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['Chrome'],
    singleRun: true,
    concurrency: Infinity,
  });
};