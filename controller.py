import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# create database
mydb = myclient["TenYearNote"]
