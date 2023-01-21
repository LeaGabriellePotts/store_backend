import pymongo
import certifi

connection_str = "mongodb+srv://TopFun:TopFun1@cluster0.8vs7v72.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCAFile=certifi.where())
db = client.get_database("OnlineStore")