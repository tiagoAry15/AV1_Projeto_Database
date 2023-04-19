
import math

import pandas as pd

from HashIndexExample.src.classes.Parameters import Parametros

from HashIndexExample.src.classes.Pagina import Pagina
from HashIndexExample.src.utils.HashUtil import HashUtil
from HashIndexExample.src.classes.Bucket import Bucket
from HashIndexExample.src.classes.Tabela import Tabela
from HashIndexExample.src.classes.Tupla import Tupla


class Controller:
    def __init__(self) -> None:
        self.lista_buckets = []
        self.tabela = Tabela()
        self.paginas = []
        self.params = Parametros()
        self.Hash = HashUtil()
        pass

    def load_file(self, file_lines, params):
        self.params = params
        self.lista_buckets = []
        pagina_atual = 0
        contador = 1
        self.tabela = Tabela()
        self.paginas = [Pagina(i)

                        for i in range(math.ceil(len(file_lines)/self.params.tamanho_pagina))]

        self.Hash.mod = params.total_buckets
        for line in file_lines:

            line = line.decode('utf-8').replace('\n', '')
            line = line.replace('\r', '')

            self.tabela.tuplas.append(
                Tupla(pagina_atual, line))
            
            self.paginas[pagina_atual].registros.append(line)
        # Cria as tuplas em suas respectivas paginas
            if contador == self.params.tamanho_pagina:
                pagina_atual += 1
                contador = 1
            else:
                contador += 1

        
        # Criação de Buckets
        self.criar_buckets()
        self.criar_indices_hash()
        # Criação do indice HASH
        response = {
            'response':{'colisoes': self.mostrar_colisoes,
                        'overflows': self.mostrar_overflows}
           
        }
        return response

    def criar_buckets(self):
        contador = 0
        for contador in range(math.floor(self.params.total_buckets)):
            b = Bucket(contador, self.params.tamanho_bucket)
            self.lista_buckets.append(b)

    def criar_indices_hash(self):
        for pagina in self.paginas:
            for registro in pagina.registros:
                self.lista_buckets[self.Hash.hash(registro)].add(
                    Tupla(pagina.id, registro))

    def buscar(self, palavra):
        bucket = self.lista_buckets[self.Hash.hash(palavra)]
        errorSearch = None

        result = None
        if bucket.tuplas == []:
            return {"result": result, "errorSearch":errorSearch }
        
        for tupla in bucket.tuplas:
            if tupla.value == palavra:
                result = Tupla(tupla.key, palavra)
                break
               


        return {"result":result, "errorSearch":errorSearch }
                

    def mostrar_registros(self, tuples_quant):
        tuples_list = []
        acesso_disco = 1
        pagina_atual = 0
        for tuples in range(tuples_quant):
            if self.tabela.tuplas[tuples].key != pagina_atual:
                pagina_atual +=1
                acesso_disco +=1

            tuples_list.append(self.tabela.tuplas[tuples])
        return {"list": tuples_list, "acessoDisco":acesso_disco}

    def mostrar_colisoes(self):
        return sum([bucket.getCollisions() for bucket in self.lista_buckets])

    def mostrar_overflows(self):
        return sum([bucket.getOverflows() for bucket in self.lista_buckets])
