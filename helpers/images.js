// Require models
var models = require('../models');

// Call python script on upload
module.exports = {
    ocr: (callback) =>{
		models.Image.find({}, {}, {limit: 1, sort : { timestamp : -1 }},
			(err, image) =>{
				if (err) throw err;
			
			var {PythonShell} = require('python-shell');

			// Take the path of last uploaded file
			var uploadedFilePath = "public/upload/"+(image[0]["filename"]);

			// Take the description/expected answer from the last uploaded file
			var keywords = image[0]["description"];

			// pass these variables to the python script
			var options = {
		    mode: 'text',
		    args: [uploadedFilePath, keywords]
		};

		
		///// When starting for first time use a path which is known for ex:
		//'/home/saurabh/Desktop/Web-Development-with-MongoDB-and-Node-Third-Edition-master/Chapter07/scripts/test.jpeg'

		///// or
		//"/home/saurabh/ocr-and-answer-evaluation/public/upload/3upmam.jpeg"

		// After uploading the first image, you will now have atleast one image in the database and won't get the error, so replace the above path with:
		//"public/upload/"+(image[0]["filename"])
		
		// Same with description
		//image[0]["description"]
		// when uploading first file, use the string i.e. expected answer for ex.
		//"Conductor in magnetic field produce voltage"


		// Run the python script with parameters as specified by options as stated above
		PythonShell.run('scripts/script.py', options, function (err, results) {
		    if (err) throw err;
		    // results is an array consisting of messages collected during execution
		    callback(null, results);
			});
		});
    }
};