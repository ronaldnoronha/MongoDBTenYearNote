from mongo import Mongo
import time
from datetime import datetime

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

ticks = Mongo("TenYearNote")

ticks.create_db()
ticks.create_col('raw_ticks')
mycol = ticks.mycol
# delete entries
x = mycol.delete_many({})
print(x.deleted_count," deleted")

# add documents
t1 = time.time()


mylist = []

with open('test_file.txt') as f:
    counter = 0
    lines = f.readlines()
    instrument='TYAH16'

    for i in lines:
        if counter > 0:
            words = i.split(", ")
            my_dict = {'datetime':convert_to_datetime(words[0], words[1]).__str__(),'instrument':instrument,
                      'price':words[2],'volume':int(words[6]),'delta':int(words[9]) - int(words[8])}

            mylist.append(my_dict)
        counter += 1


ticks.add_documents(mylist)

t2 = time.time()

print(t2-t1," seconds")

print(mycol.count_documents({}).__str__()," entries")


