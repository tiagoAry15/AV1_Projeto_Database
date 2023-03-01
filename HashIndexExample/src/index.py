
from AV1_Projeto_Database.HashIndexExample.src.classes.Tabela import Tabela
from HashIndexExample.src.classes.Tupla import Tupla


PAGE_SIZE = 10

file = open("AV1_Projeto_Database\HashIndexExample\words_alpha.txt", "r")

tabela = Tabela()


def load_file():
    current_page = 0
    counter = 1
    for line in file:

        tabela.registros.append(Tupla(current_page, line))

        if counter == PAGE_SIZE:
            current_page += 1
            counter = 1
        else:
            counter += 1
