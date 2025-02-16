// Some necessary modules
const express = require("express");
var config = require("./server/configure");
var mongoose = require("mongoose");

// Database - loginapp
mongoose.connect("mongodb://localhost/loginapp");
// Create connection
var db = mongoose.connection;

// Create app
let app = express();
app = config(app);
app.set("port", process.env.PORT || 3000);
app.set("views", `${__dirname}/views`);

// Configure app and get it running
app = config(app);

var server = app.listen(app.get("port"), () => {
  console.log("Server up: http://localhost:" + app.get("port"));
});
