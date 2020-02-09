import pymongo

class Mongo:
    # import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = None
    mycol = None

    def __init__(self, name):
        self.name = name

    def create_db(self):

        # create database
        self.mydb = self.myclient[self.name]
        print('Database created!')

    def create_col(self, collection):

        # create collection
        self.mycol = self.mydb[collection]

    def add_documents(self, documents):

        self.mycol.insert_many(documents)
