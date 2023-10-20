from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        "mongodb+srv://Bogdan:gypsy_king21@bogdan.qbagtab.mongodb.net/?retryWrites=true&w=majority")

    db = client.dz_10
    return db
