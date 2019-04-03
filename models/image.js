// Use mongoose as a client for MongoDB
const mongoose = require('mongoose'),
    Schema = mongoose.Schema,
    path = require('path');

// Image schema
const ImageSchema = new Schema({
    title:          { type: String },
    description:    { type: String },
    filename:       { type: String },
    timestamp:      { type: Date, 'default': Date.now }
});

ImageSchema.virtual('uniqueId')
.get(function(){
    return this.filename.replace(path.extname(this.filename), '');
});

// Export model
module.exports = mongoose.model('Image', ImageSchema);
