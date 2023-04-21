#Classe ZoologicoCLI
from animal import Animal
from cuidador import Cuidador
from habitat import Habitat
from zoologico_dao import ZoologicoDAO


class ZoologicoCLI:

    #ATRIBUTOS
    zoologicoDAO = ZoologicoDAO() #objeto para operar o banco de dados




    #CONSTRUTOR

    def __init__(self):
        pass




    #METODOS

    #Metodo para gerenciar o menu do sistema
    def menu(self):
        print("Escolha o que fazer:")
        print("1 - criar um cuidador, habitat(s) e um animal (create)")
        print("2 - ler um animal (read)")
        print("3 - atualizar um animal (update)")
        print("4 - deletar um animal (delete)")

        escolha = input("Digite o código: ")

        if escolha == "1":
            print("Você escolheu criar cuidador, habitat(s) e um animal (create)")
            self.createAnimal() #chamando o metodo de criar o animal
        elif escolha == "2":
            print("Você escolheu ler um animal (read)")
        elif escolha == "3":
            print("Você escolheu atualizar um animal (update)")
        elif escolha == "4":
            print("Você escolheu deletar um animal (delete)")

    #Metodo para criar um cuidador, habitat(s) e um animal
    def createAnimal(self):

        #Criando o cuidador

        print("Primeiro, crie um cuidador.")

        idCuidador = input("Entre com o id do cuidador: ")
        nomeCuidador = input("Entre com o nome do cuidador: ")
        documentoCuidador = input("Documento cuidador: ")

        cuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)


        #Criando a lista de habitats

        listaHabitatsAnimal = []

        flag = "1" #flag para determinar quando parar de criar habitats, 1 eh sim e 0 eh nao

        while(flag == "1"):
            print("Criando um habitat.")

            idHabitat = input("Entre com o id do habitat: ")
            nomeHabitat = input("Entre com o nome do habitat: ")
            tipoAmbienteHabitat = input("Entre com o tipo de ambiente do habitat: ")

            habitat = Habitat(idHabitat, nomeHabitat, tipoAmbienteHabitat, cuidador)

            listaHabitatsAnimal.append(habitat) #adicionando o habitat ah lista

            flag = input("Deseja criar mais um habitat? (1 = sim, 0 = nao)")


        #Criando o animal

        print("Agora crie um animal.")

        idAnimal = input("Entre com o id do animal: ")
        nomeAnimal = input("Entre com o nome do animal: ")
        especieAnimal = input("Entre com a especie do animal: ")
        idadeAnimal = input("Entre com a idade do animal: ")

        animal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, listaHabitatsAnimal)

