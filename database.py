import os
import json


def set(key: str, val):
    datab = open(os.path.join(os.getcwd(), "database.json"), "r")
    db = json.load(datab)
    db[key] = val
    storage = open(os.path.join(os.getcwd(), "database.json"), "w")
    storage.write(json.dumps(db)+"\n")
    storage.close()
    return True


def get(key: str):
    datab = open(os.path.join(os.getcwd(), "database.json"), "r")
    database = json.load(datab)
    return database[key]
