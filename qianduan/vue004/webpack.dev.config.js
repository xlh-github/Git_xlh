

module.exports = {
    entry: {
        'main': './main.js',
    },
    output: {
        'filename': './bundle.js',
    },
    watch: true,

        module: {
        loaders: [
            {

                test: /\.css$/, //正则表达式
                loader: 'style-loader!css-loader'
            },

            {
                test:/\.(jpg|png|jpeg|gif|svg)$/,
                loader:'url-loader?limit=4000&name=pic/[name].[ext]'
            },
            {
                test:/\.less$/,
                loader:'style-loader!css-loader!less-loader'
            }
        ]
    }
};