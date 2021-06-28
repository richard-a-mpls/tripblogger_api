import pymongo
import os
from bson.objectid import ObjectId

class MongoInterface:

    mongo_uri = "mongodb://mongo:27017/"
    my_db = None

    def get_session(self, session_id):
        my_col = self.my_db["sessions"]
        my_result = my_col.find_one({ "_id": ObjectId(session_id)})
        res_json = {"location": os.environ["host_url"] + "sessions/" + str(my_result["_id"])}
        return res_json

    def find_token_session(self, identity_token, identity_issuer):
        print ("find from " + self.mongo_uri)
        print ("Find token session " + identity_token + ":" + identity_issuer)
        my_col = self.my_db["sessions"]
        print ("got col")
        my_result = my_col.find_one({ "identity_token": identity_token, "identity_issuer": identity_issuer})
        print ("got result")
        try:
            res_json = {"location": os.environ["host_url"] + "sessions/" + str(my_result["_id"])}
            return my_result
        except:
            print ("no session found")
            return None


    def create_session(self, session_json):
        print ("find from " + self.mongo_uri)
        my_col = self.my_db["sessions"]
        id = my_col.insert_one(session_json)
        return id.inserted_id


    def get_tasks(self):
        my_col = self.my_db["customers"]
        my_list = my_col.find()
        my_results = list()
        for l in my_list:
            res_json = {"location": os.environ["host_url"] + "tasks/" + str(l["_id"]), "name": l["name"], "address": l["address"]}
            my_results.append(res_json)
        return my_list.count(), my_results

    def get_task(self, task_id):
        my_col = self.my_db["customers"]
        # { <field>: { $eq: <value> } }
        my_result = my_col.find_one({ "_id": ObjectId(task_id)})
        print ("myresult: " + str(my_result))
        print (my_result["_id"])
        res_json = {"location": os.environ["host_url"] + "tasks/" + str(my_result["_id"]),
                    "name": my_result["name"],
                    "address": my_result["address"]}
        return res_json

    def create_task(self, task_json):
        my_col = self.my_db["customers"]
        id = my_col.insert_one(task_json)
        return id.inserted_id

    def delete_task(self, task_id):
        my_col = self.my_db["customers"]
        res = my_col.delete_one({ "_id": ObjectId(task_id)})
        return res.deleted_count

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://mongo:27017/")
        self.my_db = myclient["mydatabase"]