from datetime import date
from glob import glob
from itertools import count
import json
from operator import truediv
from sqlite3 import Date
from numpy import append
import pandas as pd
import asyncio
import threading
from time import sleep
from datetime import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from elasticsearch import Elasticsearch
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.clustering import KMeans
print("-------- APPLICATION START PRIMA ATT -----------")


#create elasticsearch index
ADDRESS = "http://elasticsearch:9200"
ELASTICINDEX = "geolocation"
AIRPORT = "airportcataniafontanarossa"
STATION = "centralstation"
EUROPA = "peuropa"
LICUTI = "sangiovannilicuti"
VERGA = "pgiovanniverga"
BELLINI = "bellinigarden"
CENTRO = "oldtowncentre"


#Elastic Geo mapping
mapping = {
    "mappings":{
        "properties": {
            "timestamp": {
            "type": "date"
            },
            "location" : {
                "type" : "geo_point"
            },
            "id": {
            "type": "long"
            },
            "height": {
            "type": "float"
            },
            "weight": {
            "type": "float"
            }
        }
    }
}

altezzaAirport = []
pesoAirport = []
altezzaAirport.append(190)
pesoAirport.append(80)
altezzaAirport.append(155)
pesoAirport.append(50)

altezzaStation = []
pesoStation = []
altezzaStation.append(190)
pesoStation.append(80)
altezzaStation.append(155)
pesoStation.append(50)

altezzaEuropa = []
pesoEuropa = []
altezzaEuropa.append(190)
pesoEuropa.append(80)
altezzaEuropa.append(155)
pesoEuropa.append(50)

altezzaLicuti = []
pesoLicuti = []
altezzaLicuti.append(190)
pesoLicuti.append(80)
altezzaLicuti.append(155)
pesoLicuti.append(50)

altezzaVerga = []
pesoVerga = []
altezzaVerga.append(190)
pesoVerga.append(80)
altezzaVerga.append(155)
pesoVerga.append(50)

altezzaBellini = []
pesoBellini = []
altezzaBellini.append(190)
pesoBellini.append(80)
altezzaBellini.append(155)
pesoBellini.append(50)

altezzaCentro = []
pesoCentro = []
altezzaCentro.append(190)
pesoCentro.append(80)
altezzaCentro.append(155)
pesoCentro.append(50)


def checkAirport(lat,lon,altezza,peso):
    if lat >= 37.4573 and lat <= 37.4766:
        if lon >= 15.0489 and lon <= 15.0839:
            global altezzaAirport
            global pesoAirport
            altezzaAirport.append(altezza)
            pesoAirport.append(peso)

            #vertex clustering (per document)
            d = {"altezzaAirport": altezzaAirport,"pesoAirport":pesoAirport}
            df = pd.DataFrame(d)
            dataframeAirport = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaAirport", "pesoAirport"], outputCol="features")
            new_df = vecAssembler.transform(dataframeAirport)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
            #print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=AIRPORT, document=data)
            #print(resp['result'])
            es.indices.refresh(index=AIRPORT)
            return True 
    return False   

def checkStation(lat,lon,altezza,peso):
    if lat >= 37.5062 and lat <= 37.5086:
        if lon >= 15.0976 and lon <= 15.1012:
            global altezzaStation
            global pesoStation
            altezzaStation.append(altezza)
            pesoStation.append(peso)

            #vertex clustering (per document)
            d = {"altezzaStation": altezzaStation,"pesoStation":pesoStation}
            df = pd.DataFrame(d)
            dataframeStation = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaStation", "pesoStation"], outputCol="features")
            new_df = vecAssembler.transform(dataframeStation)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
            #print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=STATION, document=data)
            #print(resp['result'])
            es.indices.refresh(index=STATION)
            return True 
    return False 

def checkEuropa(lat,lon,altezza,peso):
    if lat >= 37.5150 and lat <= 37.5188:
        if lon >= 15.1035 and lon <= 15.1080:
            global altezzaEuropa
            global pesoEuropa
            altezzaEuropa.append(altezza)
            pesoEuropa.append(peso)

            #vertex clustering (per document)
            d = {"altezzaEuropa": altezzaEuropa,"pesoEuropa":pesoEuropa}
            df = pd.DataFrame(d)
            dataframeEuropa = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaEuropa", "pesoEuropa"], outputCol="features")
            new_df = vecAssembler.transform(dataframeEuropa)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
            #print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=EUROPA, document=data)
            #print(resp['result'])
            es.indices.refresh(index=EUROPA)
            return True 
    return False

def checkLicuti(lat,lon,altezza,peso):
    if lat >= 37.5196 and lat <= 37.5206:
        if lon >= 15.1091 and lon <= 15.1120:
            global altezzaLicuti
            global pesoLicuti
            altezzaLicuti.append(altezza)
            pesoLicuti.append(peso)

            #vertex clustering (per document)
            d = {"altezzaLicuti": altezzaLicuti,"pesoLicuti":pesoLicuti}
            df = pd.DataFrame(d)
            dataframeLicuti = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaLicuti", "pesoLicuti"], outputCol="features")
            new_df = vecAssembler.transform(dataframeLicuti)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
           # print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=LICUTI, document=data)
            #print(resp['result'])
            es.indices.refresh(index=LICUTI)
            return True 
    return False

def checkVerga(lat,lon,altezza,peso):
    if lat >= 37.5133 and lat <= 37.5160:
        if lon >= 15.0915 and lon <= 15.0946:
            global altezzaVerga
            global pesoVerga
            altezzaVerga.append(altezza)
            pesoVerga.append(peso)

            #vertex clustering (per document)
            d = {"altezzaVerga": altezzaVerga,"pesoVerga":pesoVerga}
            df = pd.DataFrame(d)
            dataframeVerga = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaVerga", "pesoVerga"], outputCol="features")
            new_df = vecAssembler.transform(dataframeVerga)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
            #print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=VERGA, document=data)
            #print(resp['result'])
            es.indices.refresh(index=VERGA)
            return True 
    return False

def checkBellini(lat,lon,altezza,peso):
    if lat >= 37.5078 and lat <= 37.5147:
        if lon >= 15.0800 and lon <= 15.0907:
            global altezzaBellini
            global pesoBellini
            altezzaBellini.append(altezza)
            pesoBellini.append(peso)

            #vertex clustering (per document)
            d = {"altezzaBellini": altezzaBellini,"pesoBellini":pesoBellini}
            df = pd.DataFrame(d)
            dataframeBellini = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaBellini", "pesoBellini"], outputCol="features")
            new_df = vecAssembler.transform(dataframeBellini)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
            #print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=BELLINI, document=data)
            #print(resp['result'])
            es.indices.refresh(index=BELLINI)
            return True 
    return False

def checkCentro(lat,lon,altezza,peso):
    if lat >= 37.5000 and lat <= 37.5039:
        if lon >= 15.0853 and lon <= 15.0905:
            global altezzaCentro
            global pesoCentro
            altezzaCentro.append(altezza)
            pesoCentro.append(peso)

            #vertex clustering (per document)
            d = {"altezzaCentro": altezzaCentro,"pesoCentro":pesoCentro}
            df = pd.DataFrame(d)
            dataframeCentro = spark.createDataFrame(df)
            vecAssembler = VectorAssembler(inputCols=["altezzaCentro", "pesoCentro"], outputCol="features")
            new_df = vecAssembler.transform(dataframeCentro)
            kmeans = KMeans(k=2, seed=1)  
            model = kmeans.fit(new_df.select('features'))
            predictions = model.transform(new_df)
            predictions = predictions.groupBy("prediction").count().withColumnRenamed("count", "count")
            #print(predictions)
            predictions.show()
            pandasDF = predictions.toPandas()
            #print(pandasDF)
            row1 = pandasDF.iloc[[0]]
            row2 = pandasDF.iloc[[1]]
            numDonne = row1.iloc[0,1]
            numUomini = row2.iloc[0,1]
            data = json.dumps({"timestamp" : datetime.now().isoformat(), "men": int(numUomini),"women": int(numDonne)})
            #print(data)
            resp = es.index(index=CENTRO, document=data)
            #print(resp['result'])
            es.indices.refresh(index=CENTRO)
            return True 
    return False                      



def elaborate(batch_df: DataFrame, batch_id: int):
    print("-----------------ELABORATE FUNCTION START------------------")
    pandasDF = batch_df.select("value").toPandas()
    if(pandasDF.empty == False):
        row = pandasDF.iloc[[0]]
        payload = row.iloc[0,0]
        #print("!!!!! payload: ")
        #print(payload)
        #print("!!! geo OBJ")
        geo = json.loads(payload)
        id = geo["id"]
        timestamp = geo["timestamp"]
        geo["timestamp"] = datetime.now().isoformat()
        lat = float(geo["lat"])
        lon = float(geo["lon"])
        altezza = float(geo["altezza"])
        peso = float(geo["peso"])
        #print("lat -> " + str(lat) + " lon -> " + str(lon))
        if((checkAirport(lat,lon,altezza,peso) == False) and (checkBellini(lat,lon,altezza,peso) == False) and (checkCentro(lat,lon,altezza,peso) == False) and (checkEuropa(lat,lon,altezza,peso) == False) and (checkLicuti(lat,lon,altezza,peso) == False) and (checkStation(lat,lon,altezza,peso) == False) and (checkVerga(lat,lon,altezza,peso) == False)):
            print("!!!!!!!!!!!!!!!!!!!!!!!! PERSONA FUORI DAI PUNTI DI INTERESSE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
            return
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!! UNA PERSONA TROVATA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            location = str(geo["lat"]) + ", " + str(geo["lon"])
            data = json.dumps({"timestamp" : geo["timestamp"],"location" : str(location),"id" : geo["id"],"height" : geo["altezza"],"weight" : geo["peso"]})
            resp = es.index(index=ELASTICINDEX, document=data)
            #print(resp['result'])
            es.indices.refresh(index=ELASTICINDEX)
            


           
               
            
    

#print("-------- Try connection -----------")

kafkaServer="broker:29092"
topic = "mytopic"

#print("-------- connection OK -----------")
#elasticsearch configuration 
#print("try connection to elasticsearch")
es = Elasticsearch(
    ADDRESS,
    verify_certs=False
)
#print(es)
es.indices.create(index=ELASTICINDEX, body=mapping, ignore=400)
es.indices.create(index=AIRPORT, body=mapping, ignore=400)
es.indices.create(index=STATION, body=mapping, ignore=400)
es.indices.create(index=EUROPA, body=mapping, ignore=400)
es.indices.create(index=LICUTI, body=mapping, ignore=400)
es.indices.create(index=VERGA, body=mapping, ignore=400)
es.indices.create(index=BELLINI, body=mapping, ignore=400)
es.indices.create(index=CENTRO, body=mapping, ignore=400)



#print("indice creato")

#spark context creation

#print("-------- SparkContextCreation -----------")

sc = SparkContext(appName="PythonStructuredStreamsKafka")
spark = SparkSession(sc)
sc.setLogLevel("WARN") 

#print("-------- spark read -----------")

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafkaServer) \
    .option("subscribe", topic) \
    .load()
    
#print("-------- spark select -----------")


df.selectExpr("CAST(timestamp AS STRING)","CAST(value AS STRING)") \
    .writeStream \
    .foreachBatch(elaborate) \
    .start() \
    .awaitTermination()
    
    


