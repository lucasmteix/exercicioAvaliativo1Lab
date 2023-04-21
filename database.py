#Classe Database

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['zoologico']

animais = db.animais

results = animais.find({"nome": "mel"})

print(results)

newdoc = {

    "_id": "1",
    "nome": "zeze"
}

result = db.animais.insert_one(newdoc)

print(result)

