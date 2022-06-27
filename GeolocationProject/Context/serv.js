var startGeneration = require("./datagen");
var express = require("express");
var fs = require("fs");
var serv = express();
serv.get("/", function (req, res) {
    data = startGeneration()
    res.send(data);
});
serv.listen(8080);
