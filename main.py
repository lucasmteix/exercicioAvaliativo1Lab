from zoologico_cli import ZoologicoCLI
from database import Database

#programa = ZoologicoCLI()

#programa.menu()

db = Database("zoologico", "animais")

db.connect("zoologico", "animais")

animais = db.animais

newdoc = {

    "_id": "2",
    "nome": "ronaldo"
}

result = animais.insert_one(newdoc)