/* jshint node: true */
'use strict';

// Some required modules
const models = require('../models'),
    async = require('async');

module.exports = (callback)=>{

    async.parallel([
        (next)=>{
            models.Image.count({}, next); // number of images uploaded in the system
        }
    ], (err, results)=>{
        callback(null, {
            images: results[0]
        });
    });
};
