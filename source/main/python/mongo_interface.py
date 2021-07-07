import pymongo
import os
from bson.objectid import ObjectId

class MongoInterface:

    mongo_uri = "mongodb://mongo:27017/"
    my_db = None

    def get_profile_by_id(self, profile_id):
        my_col = self.my_db["profile"]
        my_result = my_col.find_one({"_id": ObjectId(profile_id)})
        if my_result is None:
            print ("profile not found")
            return
        return my_result

    def get_profile_by_identity(self, identity_issuer, identity_id):
        my_col = self.my_db["profile"]
        my_result = my_col.find_one({"identity_issuer": identity_issuer, "identity_id": identity_id})
        return my_result

    def create_profile(self, profile_json):
        print ("find from " + self.mongo_uri)
        my_col = self.my_db["profile"]
        id = my_col.insert_one(profile_json)
        return id.inserted_id

    def patch_profile(self, profile_id, attributes_json):
        print ("patch profile ")
        print ("profile id: " + str(profile_id))
        print ("json: " + str(attributes_json))

        my_col = self.my_db["profile"]

        filter = {"_id": ObjectId(profile_id)}
        new_values = {"$set": attributes_json}
        my_result = my_col.update_one(filter, new_values)
        cursor = my_col.find()
        print ("printing found")
        for record in cursor:
            print(record)
        print ("done printing found")

        print (str(my_result.matched_count))
        print (str(my_result.upserted_id))
        print (str(my_result.modified_count))

        returned_profile = self.get_profile_by_id(profile_id)
        print ("returned profile: " + str(returned_profile))

    def get_session_by_id(self, session_id):
        my_col = self.my_db["sessions"]
        my_result = my_col.find_one({ "_id": ObjectId(session_id)})
        res_json = {"location": os.environ["host_url"] + "sessions/" + str(my_result["_id"])}
        return res_json

    def get_session_by_api_token(self, api_token):
        my_col = self.my_db["sessions"]
        my_result = my_col.find_one({ "api_token": api_token})
        return my_result

    def delete_session_by_api_token(self, api_token):
        found_session = self.get_session_by_api_token(api_token)
        if found_session is None:
            print("could not find session " + api_token + " to delete, blindly returning success")
            return
        print("deleting session:  " + str(found_session))
        my_col = self.my_db["sessions"]
        res = my_col.delete_one({ "_id": found_session["_id"]})
        print("deleted " + str(res.deleted_count) + " sessions.")

    def find_token_session(self, identity_token, identity_issuer):
        print ("find from " + self.mongo_uri)
        print ("Find token session " + identity_token + ":" + identity_issuer)
        my_col = self.my_db["sessions"]
        print ("got col")
        my_result = my_col.find_one({ "identity_token": identity_token, "identity_issuer": identity_issuer})
        print ("got result")
        try:
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