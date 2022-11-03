from pymongo import MongoClient
import dns
# client = MongoClient("mongodb+srv://admin-ken:cornelltech2022@cluster0.rsxddxh.mongodb.net/?retryWrites=true&w=majority")

client = MongoClient("mongodb+srv://admin-ken:cornelltech2022@cluster0.rsxddxh.mongodb.net/?retryWrites=true&w=majority")
db = client.crashHistoryDB

# collection_name = db["api_crash_history"]
collection_name = db["api_crash_history_1_1"]
intersection_dangerousity = db["intersect_dangerousity_1_0"]
print("connected to mongodb")

# get lat, long
# count = 0
# for record in intersection_dangerousity.find():
#     coord_str = record["coordinates"][1:-1]
#     coord_str_list = coord_str.split(",")
#     lat, lng = float(coord_str_list[0]), float(coord_str_list[1])

#     myquery = { "_id": record["_id"] }
#     newvalue = { "$set": { "loc": [lng, lat] } }

#     intersection_dangerousity.update_one(myquery, newvalue)
#     count += 1
#     print(record["_id"], count)

# print("success")