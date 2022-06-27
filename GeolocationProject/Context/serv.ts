const startGeneration = require("./datagen");
const express = require("express");
const fs = require("fs");
const serv = express();

serv.get("/",(req,res) => {
    const data = fs.readFileSync("./data.txt", {encoding: 'utf-8'});
    res.send(data);
    
});


startGeneration();

serv.listen(8080);