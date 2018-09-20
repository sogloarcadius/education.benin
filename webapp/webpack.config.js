var path = require('path')
var webpack = require('webpack')

function resolve (dir) {
	return path.join(__dirname, dir)
}

module.exports = {
	entry: './src/main.js',
	output: {
		path: path.resolve(__dirname, './build'),
		publicPath: '/build/',
		filename: 'build.js'
	},
	module: {
		rules: [
			{
				test: /\.vue$/,
				loader: 'vue-loader',
				options: {
					loaders: {
            js: 'babel-loader?presets[]=es2015'
					}
					// other vue-loader options go here
				}
			},
			{
				test: /\.js$/,
				loader: 'babel-loader',
				exclude: /node_modules/,
				query: {
          			presets: ['es2015']
        		}	
			},
			{
				test: /\.css$/,
				loader: "style-loader!css-loader"
			},
			{
				test: /\.(png|woff|woff2|eot|ttf|svg)$/,
				loader: 'url-loader'
			}
		]
	},
	resolve: {
		extensions: ['.js', '.vue', '.json', '.svg'],
		alias: {
			'vue$': 'vue/dist/vue.esm.js',
			'@': resolve('src'),
		}
	},
	devServer: {
		historyApiFallback: true,
		noInfo: true
	},
	performance: {
		hints: false
	},
	devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
	module.exports.devtool = '#source-map'
	// http://vue-loader.vuejs.org/en/workflow/production.html
	module.exports.plugins = (module.exports.plugins || []).concat([
		new webpack.DefinePlugin({
			'process.env': {
				NODE_ENV: '"production"'
			}
		}),
		new webpack.ProvidePlugin({
				'Promise': 'es6-promise',
				'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch',
				 $: 'jquery',
				 jquery: 'jquery',
				 _: 'lodash',
				 jsonPath: 'JSONPath'
		}),
		new webpack.optimize.UglifyJsPlugin({
			sourceMap: true,
			compress: {
				warnings: false
			}
		}),
		new webpack.LoaderOptionsPlugin({
			minimize: true
		})
	])
} else if (process.env.NODE_ENV === 'development') {
	module.exports.devtool = '#source-map'
	module.exports.plugins = (module.exports.plugins || []).concat([
		new webpack.LoaderOptionsPlugin({
			debug: true
		}),
		new webpack.ProvidePlugin({
				'Promise': 'es6-promise',
				'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch',
				 $: 'jquery',
				 jquery: 'jquery',
				 _: 'lodash',
				 jsonPath: 'JSONPath'
		})
	])
}
