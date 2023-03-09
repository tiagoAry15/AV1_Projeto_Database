
import math

import pandas as pd
from classes.Pagina import Pagina
from Util.HashUtil import HashUtil
from classes.Bucket import Bucket
from classes.Tabela import Tabela
from classes.Tupla import Tupla


PAGE_SIZE = 370
TUPLES_P_BUCKETS = 100
BUCKET_QUANT = 370000/TUPLES_P_BUCKETS


arquivo = open(
    "AV1_Projeto_Database\HashIndexExample\Resources\words_alpha.txt", "r")
Bucket_List = []
tabela = Tabela()


def load_file(file):
    current_page = 0
    counter = 1

    lines = file.readlines()
    pages = [Pagina(i)

             for i in range(math.ceil(len(lines)/PAGE_SIZE))]

    for line in lines:

        tabela.registros.append(Tupla(current_page, line))

        pages[current_page].tuplas.append(Tupla(current_page, line))
    # Cria as tuplas em suas respectivas paginas
        if counter == PAGE_SIZE:
            current_page += 1
            counter = 1
        else:
            counter += 1

    file.close()
    # Criação de Buckets
    create_buckets()
    create_hash_indexes()
    # Criação do indice HASH


def create_buckets():
    counter = 0
    for counter in range(math.floor(BUCKET_QUANT)):
        b = Bucket(counter, TUPLES_P_BUCKETS)
        Bucket_List.append(b)


def create_hash_indexes():
    for tupla in tabela.registros:
        Bucket_List[HashUtil.hash(tupla.value)].add(tupla)


def search_data(palavra):
    bucket = Bucket_List[HashUtil.hash(palavra)]

    if bucket.tuplas == []:
        return "palavra não encontrada"
    else:
        while True:
            for tupla in bucket.tuplas:
                if tupla.value == palavra:
                    return "palavra = " + palavra + ", pagina = " + str(tupla.key)

            if bucket.nextBucket != None:
                bucket = bucket.nextBucket
            else:
                return "palavra não encontrada"


def show_tuples(tuples_quant):
    df_tuples = pd.DataFrame()
    for tuples in range(tuples_quant):
        df_tuples.add(tabela.registros[tuples])
    return df_tuples


def show_collisions():
    return sum([bucket.getCollisions() for bucket in Bucket_List])


def show_overflows():
    return sum([bucket.getOverflows() for bucket in Bucket_List])


load_file(arquivo)

search_data('aahed\n')
print(show_collisions())
print(show_overflows())
