// Some required modules
const Stats = require('./stats'),
    Images = require('./images'),
    async = require('async');

module.exports = (viewModel, callback)=>{
    async.parallel([
        (next)=>{
            Stats(next); // Stats about the system i.e. number of uploads
        },
        (next)=>{
            Images.ocr(next); // Output of the python script
        }
    ], (err, results)=>{
        // store both the results and use callback
        viewModel.sidebar = {
            stats: results[0],
            ocr: results[1]
        };

        callback(viewModel);
    });
};