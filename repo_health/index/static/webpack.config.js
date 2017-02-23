const webpack = require('webpack');
const ProgressBarPlugin = require('progress-bar-webpack-plugin');
const path = require('path');
const { argv } = require('yargs');

const baseConfig = {
  entry: {
    app: ['./client/src/main.module.js']
  },

  output: {
    path: path.join(__dirname, '/dist/js'),
    publicPath: 'js/',
    filename: '[name].js'
  },

  resolve: {
    modules: [
      path.resolve('./client/src'),
      path.resolve('./client/assets'),
      path.resolve('./node_modules')
    ],
    extensions: ['.js', '.html']
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        include: [
          path.resolve(__dirname, 'client/src'),
        ],
        loader: 'babel-loader'
      },
      {
        test: /\.html$/,
        loader: 'html-loader'
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },

  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: 'vendor',
      minChunks(module) {
        return module.context && module.context.indexOf('node_modules') !== -1;
      }
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    }),
    new webpack.NoEmitOnErrorsPlugin(),
    new ProgressBarPlugin()
  ],

  node: {
    fs: 'empty',
    net: 'empty'
  }
};

const developmentConfig = Object.assign({}, baseConfig, {
  devtool: 'cheap-module-source-map',
  cache: true,
  plugins: [
    ...baseConfig.plugins,
    new webpack.LoaderOptionsPlugin({
      debug: true
    })
  ]
});

const productionConfig = Object.assign({}, baseConfig, {
  plugins: [
    ...baseConfig.plugins,

    new webpack.LoaderOptionsPlugin({
      minimize: true,
      debug: false
    }),

    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false,
        drop_console: true,
        unused: true
      },
      sourceMap: false,
      minimize: true,
      mangle: true
    })
  ]
});

module.exports = argv.env === 'prod' ? productionConfig : developmentConfig;
