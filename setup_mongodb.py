import pymongo
from datetime import datetime
import time

def convert_to_datetime(date, time):
    # date 2015/10/6

    date_pieces = date.split("/")
    year = int(date_pieces[0])
    month = int(date_pieces[1])
    day = int(date_pieces[2])

    # time 07:44:15.001
    time_pieces = time.split(":")
    hour = int(time_pieces[0])
    minutes = int(time_pieces[1])
    seconds = int(float(time_pieces[2]))
    milli_seconds = int(1000000*(float(time_pieces[2])-seconds))

    return datetime(year,month,day,hour,minutes,seconds,milli_seconds)

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    # create database
    mydb = myclient["mydatabase"]

    # create collection
    mycol = mydb["raw_ticks"]


    # # delete entries
    # x = mycol.delete_many({})
    # print(x.deleted_count," deleted")

    t1 = time.time()

    # insert data
    mylist = []

    with open('TYAH16.txt') as f:
        counter = 0
        lines = f.readlines()
        instrument='TYAH16'
        threshold = 3999999
        for i in lines:
            if counter > 3999999 and counter <5000000:
                words = i.split(", ")
                my_dict = {'datetime':convert_to_datetime(words[0], words[1]).__str__(),'instrument':instrument,
                          'price':words[2],'volume':int(words[6]),'delta':int(words[9]) - int(words[8])}
                mycol.insert_one(my_dict)
                mylist.append(my_dict)
            counter += 1
            if counter==threshold:
                print(threshold, " done",time.time())
                threshold += int(threshold*0.1)


    # x = mycol.insert_many(mylist)

    # mydoc = mycol.find().sort("datetime")
    #
    # for x in mydoc:
    #     print(x)
    #

    t2 = time.time()

    print(t2-t1," seconds")

    print(mycol.count().__str__()," entries")

