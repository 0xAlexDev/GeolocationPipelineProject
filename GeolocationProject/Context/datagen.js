var fs = require("fs");
var numberData = 1000;
function GetLat(latMax,latMin) {
    var lat = (Math.random() * (latMax - latMin) + latMin).toFixed(4);
    return lat;
}
function GetLon(lonMax,lonMin) {
    var lon = (Math.random() * (lonMax - lonMin) + lonMin).toFixed(4);
    return lon;
}

function GetAltezza() {
    var alt = (Math.random() * (198 - 152) + 152).toFixed(2);
    return alt;
}
function GetPeso() {
    var peso = (Math.random() * (90 - 48) + 48).toFixed(2);
    return peso;
}

function GenerateData() {
    var random = parseInt((Math.random() * (10 - 0) + 0));
    var lat;
    var lon;
    if(random >= 0 && random <=2){
        lat = GetLat(37.5289,37.5082);
        lon = GetLon(15.0977,15.0512);
    }

    else if(random == 3){
        lat = GetLat(37.4766,37.4573);
        lon = GetLon(15.0839,15.0489);
    }

    else if(random == 4){
        lat = GetLat(37.5086,37.5062);
        lon = GetLon(15.1012,15.0976);
    }

    else if(random == 5){
        lat = GetLat(37.5188,37.5150);
        lon = GetLon(15.1080,15.1035);
    }
    else if(random == 6){
        lat = GetLat(37.5206,37.5196);
        lon = GetLon(15.1120,15.1091);
    }
    else if(random == 7){
        lat = GetLat(37.5160,37.5133);
        lon = GetLon(15.0946,15.0915);
    }
    else if(random == 8){
        lat = GetLat(37.5147,37.5078);
        lon = GetLon(15.0907,15.0800);
    }

    else if(random == 9){
        lat = GetLat(37.5039,37.5000);
        lon = GetLon(15.0905,15.0853);
    }

    var data = {
        timestamp: new Date().getTime(),
        id: numberData,
        lat: lat,
        lon: lon,
        altezza: GetAltezza(),
        peso: GetPeso()
    };
    numberData += 1;
    return JSON.stringify(data);
}

function WriteData() {
    var jsonFormat = "{ \"geolocation\" : ";
    jsonFormat = jsonFormat + GenerateData();
    jsonFormat = jsonFormat + " }";
    return jsonFormat;
}
function startGen() {
    return WriteData();
}
module.exports = startGen;
