import pymongo
import os
from bson.objectid import ObjectId

class MongoInterface:

    def get_profile_by_id(self, profile_id):
        my_col = self.my_db["profile"]
        my_result = my_col.find_one({"_id": ObjectId(profile_id)})
        if my_result is None:
            print ("profile not found")
            return
        return my_result

    def get_profile_by_subject(self, subject):
        my_col = self.my_db["profile"]
        my_result = my_col.find_one({"identity_id": subject})
        return my_result

    def get_profile_by_public_project(self, project_id):
        my_col = self.my_db["project"]
        my_result = my_col.find_one({"_id": ObjectId(project_id)})
        if my_result is not None and my_result["published"]:
            my_col = self.my_db["profile"]
            my_result = my_col.find_one({"identity_id": my_result["profileId"]})
            return my_result
        return None

    def create_profile(self, profile_json):
        my_col = self.my_db["profile"]
        id = my_col.insert_one(profile_json)
        cursor = my_col.find()
        for record in cursor:
            print ("creating profile")
            print (record)

        return id.inserted_id

    def patch_profile(self, profile_id, attributes_json):
        my_col = self.my_db["profile"]

        filter = {"_id": ObjectId(profile_id)}
        new_values = {"$set": attributes_json}
        my_col.update_one(filter, new_values)
        cursor = my_col.find()
        for record in cursor:
            return record

    def create_photo(self, project_json):
        my_col = self.my_db["photos"]
        id = my_col.insert_one(project_json)
        return str(id.inserted_id)

    def get_photo(self, photo_id):
        my_col = self.my_db["photos"]
        return my_col.find_one({"_id": ObjectId(photo_id)})

    def delete_photo(self, photo_id):
        print("delete photo: " + photo_id)
        my_col = self.my_db["photos"]
        result = my_col.delete_one({"_id": ObjectId(photo_id)})

    def append_project_photo(self, project_id, photo_id):
        my_col = self.my_db["project"]
        my_col.update({"_id": ObjectId(project_id)}, {'$push': {'photoArray': photo_id}})

    def get_project(self, project_id):
        my_col = self.my_db["project"]
        print("Conn str")
        print(os.environ.get("MONGO_URI"))
        print ("find project by id of " + project_id)
        project = my_col.find_one({ "_id": ObjectId(project_id)})
        print ("project is ")
        print (project)
        projectList = my_col.find()
        print (projectList)
        return project

    def __init__(self):
        myclient = pymongo.MongoClient(os.environ.get("MONGO_URI"))
        self.my_db = myclient[os.environ.get("MONGO_DATABASE")]