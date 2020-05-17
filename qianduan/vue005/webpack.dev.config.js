const path = require('path');
module.exports = {
    entry: {
        'main': './src/main.js',
    },

    output: {

        path:path.resolve('./dist'),
        filename:'bundle.js'
    },
    watch: true,
    module: {
        loaders: [
            {

                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test:/\.(jpg|png|jpeg|gif|svg)$/,
                loader:'url-loader?limit=4000'
            },
            {
                test:/\.less$/,
                loader:'style-loader!css-loader!less-loader'
            }
        ]
    }

};