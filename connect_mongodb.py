from bson.objectid import ObjectId
from pymongo import MongoClient

def connect_mongodb(db, collection):
    mongo_client = MongoClient("mongodb://mongo_db:27017/")
    # mongo_client = MongoClient("mongodb://localhost:27017/") #local venv 실행용
    # print(mongo_client.list_database_names())
    db_instance = mongo_client[db]
    return db_instance[collection]

def insert_one(conn, data_dict):
    try:
        conn.insert_one(data_dict)
        return True
    except Exception as e:
        print("Failed Insert data : {}".format(e))
        return False

def find_boards(conn):
    board_list = conn.find()
    board_dict = dict()

    for b in board_list:
        post_id = str(b['_id'])
        del b['_id']
        board_dict[post_id] = b

    return board_dict

def update_boards(conn, post_id, data):
    try:
        query = {'_id':ObjectId(post_id)}, {'$set': data}
        conn.update_one(*query)
        return True
    except Exception as e:
        print("Failed update data : {}".format(e))
        return False

def del_boards(conn, post_id):
    try:
        del_query = {"_id":ObjectId(post_id)}
        conn.delete_one(del_query)
        return True
    except Exception as e:
        print("Failed delete data : {}".format(e))
        return False