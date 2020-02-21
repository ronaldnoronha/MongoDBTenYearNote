import pymongo

class Mongo:
    # import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = None
    mycol = None
    temp = None

    def __init__(self, name):
        self.name = name

    def create_db(self):

        # create database
        self.mydb = self.myclient[self.name]
        print('Database created!')

    def create_col(self, collection):

        # create collection
        self.mycol = self.mydb[collection]
        self.create_index_datetime()

    def create_col_temp(self):

        self.temp = self.mydb["temp"]
        self.create_index_datetime_temp()

    def add_documents(self, documents):
        self.consolidate_data(documents)

    def create_index_datetime(self):

        self.mycol.create_index('datetime')

    def add_documents_temp(self,documents):

        self.temp.insert_many(documents)

    def create_index_datetime_temp(self):

        self.temp.create_index('datetime')

    def clear_duplicates(self,instrument):

        aggregate_string = [{"$sort": {"datetime": 1}}, {"$limit": 1}]
        ts_begin_new = list(self.temp.aggregate(aggregate_string))[0]['datetime']
        aggregate_string = [{"$sort": {"datetime": -1}}, {"$limit": 1}]
        ts_end_new = list(self.temp.aggregate(aggregate_string))[0]['datetime']

        # delete
        delete_str = {'datetime':{'$gte':ts_begin_new, '$lte':ts_end_new}}
        self.mycol.delete_many(delete_str)

    def delete_temp_collection(self):

        self.temp.drop()
        self.temp = None

    def consolidate_data(self, documents):

        self.create_col_temp()
        self.add_documents_temp(documents)
        instrument = documents[0]["instrument"]
        self.clear_duplicates(instrument)
        self.transfer_documents()

    def transfer_documents(self):

        documents = self.temp.find({})
        self.mycol.insert_many(documents)
        self.delete_temp_collection()




