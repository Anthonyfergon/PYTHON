# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:36:00 2022

@author: AFG
"""

# _____________________________________________________________________
#                    MONGODB_ATLAS + STUDIO 3T + PyMONGO
#               Prepared by AnthonyCRENG28, Rabbit industries.
# _____________________________________________________________________

# ------------------------------------------------------------------------ #

#### 01 - MONGO_UNIVERSITY:
    https://learn.mongodb.com/learn/course/

#### 02 - MONGO_GLOSSARY:
    https://www.mongodb.com/docs/manual/reference/glossary/

#### 03 - MONGO_OFFICIAL_DOCUMENTATION:
    https://www.mongodb.com/docs/
    https://www.mongodb.com/docs/manual/

#### 04 - Mongo_Hierarchical_Structures:
    Mongo_Atlas{Shards:SaaS}\
        MongoDB{Core}\
            Databases{Container}\
                Collections{Groups}\
                    Documents{"Basic_Unit": 
                              Displayed JSON,
                              Stored in BSON (extension of JSON which accpets additional data types),
                              Every Doc requires an id_field aka PK,
                              Flexible_Schema: Polymorphic DataType (Date, Float, Int, etc) + Constrains
                              }

#### 04.01 MongoDB_Document_Model:
    Syntax:
        {
        "key": value,
        "key": value,
        "key" : value
        }
   Example:
        {
        "_id": 1,
        "name": "AC3 Phone",
        "colors" : ["black", "silver"],
        "price" : 200,
        "available" : true
        }
        
#### 05 - MONGO_CONNECTION_METHODS

01: Go to Mongo Atlas (UI):
    Connection string: <mongodb+srv://<username>:<password>@cluster0.a0czo3g.mongodb.net/?retryWrites=true&w=majority>
    Username:           anthonyfergon28
    Cluster:            Cluster0
    Password:           UlysesDynamics2022
    
02: Choose the Connection Method:
    
    #### 05.01 - Mongo Atlas (UI DBSaaS)
    
    #### 05.02 - Mongo Compass (Local Application)
    
    #### 05.03 - Git Bash
    
    #### 05.04 - Atlas CLI:
        Guide: https://www.mongodb.com/docs/atlas/cli/stable/command/atlas/
        # Ignite Mongo in CLI
        atlas -- e.g.: C:\Users\Asus VivoBook>atlas
        
    #### 05.05 - Mongosh:
        Guide: https://www.mongodb.com/docs/mongodb-shell/connect/#std-label-mdb-shell-connect
        # 01. Launch Mongosh Terminal
        # 02. paste : mongodb+srv://anthonyfergon28:UlysesDynamics2022$@cluster0.a0czo3g.mongodb.net/test
        # 03. help (displays the help_command_assistance)
        
        # Note: You can obtain the above Mongo_Connection_String from MongoDB_Compass (Connect/NewConnection/Cluster0(...)<click ellipsis symbol>)
        # MongoDB CLI User_Commands: C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\MongoDB
        # Create a DB
        01. You must go to Mongo Atlas to create a DB
        02. Now you are able to consult the new DB using Studio3T, jut go to the tree and rightclick (refresh)
        03. Double click on the new collec
        tion
    
    #### 05.06 - Mongo_Shell (CLI)
        # cd C:\MongoDB\mongosh-1.6.0-win32-x64\bin
        # mongosh
        
        
        
        
        
        
        
        
        
        
        # Browse Collections
        show dbs
        
        # Use the <sample_training> database
        use sample_training
        
        # Show the collections composing a DB
        show collections
        
        # find command (select)
        db.zips.find({"state": "NY"})
        it iterates through the cursor.
        
        # find and count
        db.zips.find({"state": "NY"}).count()
        db.zips.find({"state": "NY", "city": "ALBANY"})
        db.zips.find({"state": "NY", "city": "ALBANY"}).pretty()

        # INSERT NEW DOCUMENTS
        mongoimport --uri="mongodb+srv://<username>:<password>@<cluster>.mongodb.net/sample_supplies" sales.json
        1st Step: Connect to the Atlas cluster
        mongo "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/admin"
        2nd: navigate to the database that we need:
        use sample_training
        3rd Step, get a random document from the collection:
        db.inspections.findOne();
        4th Step, copy this random document, and try to insert in into the collection:
        db.inspections.insert({
              "_id" : ObjectId("56d61033a378eccde8a8354f"),
              "id" : "10021-2015-ENFO",
              "certificate_number" : 9278806,
              "business_name" : "ATLIXCO DELI GROCERY INC.",
              "date" : "Feb 20 2015",
              "result" : "No Violation Issued",
              "sector" : "Cigarette Retail Dealer - 127",
              "address" : {
                      "city" : "RIDGEWOOD",
                      "zip" : 11385,
                      "street" : "MENAHAN ST",
                      "number" : 1712
                 }
          })

        db.inspections.insert({
              "id" : "10021-2015-ENFO",
              "certificate_number" : 9278806,
              "business_name" : "ATLIXCO DELI GROCERY INC.",
              "date" : "Feb 20 2015",
              "result" : "No Violation Issued",
              "sector" : "Cigarette Retail Dealer - 127",
              "address" : {
                      "city" : "RIDGEWOOD",
                      "zip" : 11385,
                      "street" : "MENAHAN ST",
                      "number" : 1712
                 }
          })

        db.inspections.find({"id" : "10021-2015-ENFO", "certificate_number" : 9278806}).pretty()
        db.inspections.insert([ { "test": 1 }, { "test": 2 }, { "test": 3 } ])
       
        Insert three test documents but specify the _id values:
        db.inspections.insert([{ "_id": 1, "test": 1 },{ "_id": 1, "test": 2 },
                               { "_id": 3, "test": 3 }])
        
        Find the documents with _id: 1
        db.inspections.find({ "_id": 1 })
        
        Insert multiple documents specifying the _id values, and using the "ordered": false option.
        db.inspections.insert([{ "_id": 1, "test": 1 },{ "_id": 1, "test": 2 },
                               { "_id": 3, "test": 3 }],{ "ordered": false })
        Insert multiple documents with _id: 1 with the default "ordered": true setting

        db.inspection.insert([{ "_id": 1, "test": 1 },{ "_id": 3, "test": 3 }])

        View collections in the active db
        show collections

        Switch the active db to training
        use training

        View all available databases
        show dbs

#### 05.06 - PyMongo (Python Library)    

# https://www.mongodb.com/docs/drivers/pymongo/
# https://pymongo.readthedocs.io/en/stable/
# https://pymongo.readthedocs.io/en/stable/tutorial.html

This tutorial is intended as an introduction to working with MongoDB and PyMongo.

Prerequisites
Before we start, make sure that you have the PyMongo distribution installed. In the Python shell, the following should run without raising an exception:

import pymongo
This tutorial also assumes that a MongoDB instance is running on the default host and port. Assuming you have downloaded and installed MongoDB, you can start it like so:

$ mongod
Making a Connection with MongoClient
The first step when working with PyMongo is to create a MongoClient to the running mongod instance. Doing so is easy:

from pymongo import MongoClient
client = MongoClient()
The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows:

client = MongoClient('localhost', 27017)
Or use the MongoDB URI format:

client = MongoClient('mongodb://localhost:27017/')
Getting a Database
A single instance of MongoDB can support multiple independent databases. When working with PyMongo you access databases using attribute style access on MongoClient instances:

db = client.test_database
If your database name is such that using attribute style access won’t work (like test-database), you can use dictionary style access instead:

db = client['test-database']
Getting a Collection
A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database. Getting a collection in PyMongo works the same as getting a database:

collection = db.test_collection
or (using dictionary style access):

collection = db['test-collection']
An important note about collections (and databases) in MongoDB is that they are created lazily - none of the above commands have actually performed any operations on the MongoDB server. Collections and databases are created when the first document is inserted into them.

Documents
Data in MongoDB is represented (and stored) using JSON-style documents. In PyMongo we use dictionaries to represent documents. As an example, the following dictionary might be used to represent a blog post:

import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
Note that documents can contain native Python types (like datetime.datetime instances) which will be automatically converted to and from the appropriate BSON types.

Inserting a Document
To insert a document into a collection we can use the insert_one() method:

posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
ObjectId('...')
When a document is inserted a special key, "_id", is automatically added if the document doesn’t already contain an "_id" key. The value of "_id" must be unique across the collection. insert_one() returns an instance of InsertOneResult. For more information on "_id", see the documentation on _id.

After inserting the first document, the posts collection has actually been created on the server. We can verify this by listing all of the collections in our database:

db.list_collection_names()
['posts']
Getting a Single Document With find_one()
The most basic type of query that can be performed in MongoDB is find_one(). This method returns a single document matching a query (or None if there are no matches). It is useful when you know there is only one matching document, or are only interested in the first match. Here we use find_one() to get the first document from the posts collection:

import pprint
pprint.pprint(posts.find_one())
{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
The result is a dictionary matching the one that we inserted previously.

Note The returned document contains an "_id", which was automatically added on insert.
find_one() also supports querying on specific elements that the resulting document must match. To limit our results to a document with author “Mike” we do:

pprint.pprint(posts.find_one({"author": "Mike"}))
{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
If we try with a different author, like “Eliot”, we’ll get no result:

posts.find_one({"author": "Eliot"})
>>>
Querying By ObjectId
We can also find a post by its _id, which in our example is an ObjectId:

post_id
ObjectId(...)
pprint.pprint(posts.find_one({"_id": post_id}))
{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
Note that an ObjectId is not the same as its string representation:

post_id_as_str = str(post_id)
posts.find_one({"_id": post_id_as_str}) # No result
>>>
A common task in web applications is to get an ObjectId from the request URL and find the matching document. It’s necessary in this case to convert the ObjectId from a string before passing it to find_one:

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
See also When I query for a document by ObjectId in my web application I get no result
Bulk Inserts
In order to make querying a little more interesting, let’s insert a few more documents. In addition to inserting a single document, we can also perform bulk insert operations, by passing a list as the first argument to insert_many(). This will insert each document in the list, sending only a single command to the server:

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
result.inserted_ids
[ObjectId('...'), ObjectId('...')]
There are a couple of interesting things to note about this example:

The result from insert_many() now returns two ObjectId instances, one for each inserted document.

new_posts[1] has a different “shape” than the other posts - there is no "tags" field and we’ve added a new field, "title". This is what we mean when we say that MongoDB is schema-free.

Querying for More Than One Document
To get more than a single document as the result of a query we use the find() method. find() returns a Cursor instance, which allows us to iterate over all matching documents. For example, we can iterate over every document in the posts collection:

for post in posts.find():
  pprint.pprint(post)

{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['bulk', 'insert'],
 'text': 'Another post!'}
{'_id': ObjectId('...'),
 'author': 'Eliot',
 'date': datetime.datetime(...),
 'text': 'and pretty easy too!',
 'title': 'MongoDB is fun'}
Just like we did with find_one(), we can pass a document to find() to limit the returned results. Here, we get only those documents whose author is “Mike”:

for post in posts.find({"author": "Mike"}):
  pprint.pprint(post)

{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['bulk', 'insert'],
 'text': 'Another post!'}
Counting
If we just want to know how many documents match a query we can perform a count_documents() operation instead of a full query. We can get a count of all of the documents in a collection:

posts.count_documents({})
3
or just of those documents that match a specific query:

posts.count_documents({"author": "Mike"})
2
Range Queries
MongoDB supports many different types of advanced queries. As an example, lets perform a query where we limit results to posts older than a certain date, but also sort the results by author:

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
  pprint.pprint(post)

{'_id': ObjectId('...'),
 'author': 'Eliot',
 'date': datetime.datetime(...),
 'text': 'and pretty easy too!',
 'title': 'MongoDB is fun'}
{'_id': ObjectId('...'),
 'author': 'Mike',
 'date': datetime.datetime(...),
 'tags': ['bulk', 'insert'],
 'text': 'Another post!'}
Here we use the special "$lt" operator to do a range query, and also call sort() to sort the results by author.

Indexing
Adding indexes can help accelerate certain queries and can also add additional functionality to querying and storing documents. In this example, we’ll demonstrate how to create a unique index on a key that rejects documents whose value for that key already exists in the index.

First, we’ll need to create the index:

result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                  unique=True)
sorted(list(db.profiles.index_information()))
['_id_', 'user_id_1']
Notice that we have two indexes now: one is the index on _id that MongoDB creates automatically, and the other is the index on user_id we just created.

Now let’s set up some user profiles:

user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)
The index prevents us from inserting a document whose user_id is already in the collection:

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile)
Traceback (most recent call last):
DuplicateKeyError: E11000 duplicate key error index: test_database.profiles.$user_id_1 dup key: { : 212 }
See also The MongoDB documentation on indexes