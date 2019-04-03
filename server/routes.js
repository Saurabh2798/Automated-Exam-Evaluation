// Set up all the routes
const express = require('express');
    router = express.Router();
    home = require('../controllers/home');
    image = require('../controllers/image');
module.exports = (app)=>{
    router.get('/', home.index);
    router.get('/images/:image_id', image.index);
    router.post('/images', image.create);
    router.delete('/images/:image_id', image.remove);
    app.use(router);
};

