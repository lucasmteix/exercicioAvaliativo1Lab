#Classe ZoologicoDAO

class ZoologicoDAO:

    #CONSTRUTOR

    def __init__(self):
        pass




    #METODOS

    #Metodo para criar um animal no banco de dados
    def createAnimal(self, animal):
        novoDocumento = {

            "_id" : animal.id,
            "nome": animal.nome,
            "especie": animal.especie,
            "idade": animal.idade,
            "habitat": ""
        }