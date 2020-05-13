import pymongo
from pymongo import MongoClient
cluster = MongoClient("<insert your connection string>") #changed the connection string to your own!
db = cluster["<enter your database name>"] 
collection = db["<enter your collection name>"]

pipeline = [
    {"$match": {"$and" :
        [{"age": {"$gte": 20, "$lt": 30}},
        {"company": {"$in": ["PRINTSPAN", "TECHMANIA", "NEPTIDE", "MULTRON", "SKYNET", "UPDAT", "STANTON"]}},
        {"eyeColor": {"$nin": ["black", "brown"]}},
        {"friends.name": {"$regex": "^C"}},
        {"gender": "female"}
    ]}},
    {"$project": {"name": 1, "_id": 0}}
]

#returns you a cursor object so need to iterate through result to get the actual values.
result = collection.aggregate(pipeline)
for i in result:
    print (i)

print("ending")

#https://www.gitpod.io/blog/gitpodify/
#https://www.gitpod.io/docs/getting-started/
#https://www.gitpod.io/docs/git/
