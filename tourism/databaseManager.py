from xmlrpc.client import boolean

from pymongo import MongoClient
from src import Message

class MongoDBManagment:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mailDatabase']
        self.collection = self.db['mailCollection']



    def insert_message(self,mess):
        self.collection.insert_one({
            "name": mess.author_name,
            "date": mess.date,
            "text": mess.text,
            "topic_identifier": "tourism"
        })




    def print_messages(self):
         all_messages = self.collection.find({})
         print("Number of messages : " + str(all_messages.count()))
         for each_message in all_messages:
             print(each_message)

    def find_message_by_data(self, date):
        return self.collection.find({"date": date})

    def find_messages_by_author(self,author_name):
        return self.collection.find({"name": author_name})

    def count_messages_by_author(self,author_name):
        return self.collection.find({"name": author_name}).count()


    def drop_messages(self):
        self.collection.remove()

    def close(self):
        self.client.close()


if __name__ == "__main__":
    mongoDD = MongoDBManagment()


    # mess =  Message("lolo","12,23","ewqeqweqwe")
    # mongoDD.insert_message(mess)
    var = mongoDD.find_messages_by_author("lolo")
    print(var[1]["text"])

    mongoDD.print_messages()
    #mongoDD.drop_messages()
