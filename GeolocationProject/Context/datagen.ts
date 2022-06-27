const fs = require("fs");
var numberData = 1000;
var dataStock = "";

function GetLat() {
    const lat = (Math.random() * (37.59573590243416 - 37.438883664067525) + 37.438883664067525);
    return lat;
}

function GetLon() {
    const lon = (Math.random() * (15.162506103515627 - 14.996337890625002) + 14.996337890625002);
    return lon;
}

function GenerateData() : any {
    
    let data = {
        timestamp: new Date().getTime(),
        id:numberData,
        lat:GetLat(),
        lon:GetLon()
    }
    numberData += 1;
    return JSON.stringify(data);
}


function DataStock(){
    dataStock = dataStock + GenerateData() + ',';
}

/*
function AppendData(){
    let data : any = GenerateData();
    fs.appendFile("./data.txt",data,function (err) {
        if (err){
            throw err;
        } 
        else{
            //console.log("data writed");
        }
      });
}


function startGen(){
    var intervalId = setInterval(function(){
        AppendData();
    }, 2000);
}
*/
function WriteData(){
    var jsonFormat = "{ \"geolocation\" : [";
    jsonFormat = jsonFormat + dataStock
    jsonFormat = jsonFormat + "] }";
    fs.writeFile("./data.txt",jsonFormat,function (err) {
        if (err){
            throw err;
        } 
        else{
            //console.log(dataStock + "\n\n\n");
            dataStock = "";
        }
    });
}

function startGen(){
    var intervalId = setInterval(function(){
        WriteData();
    }, 4000);

    var dataStockInterval = setInterval(function(){
        DataStock();
    }, 149);
}


module.exports = startGen;
