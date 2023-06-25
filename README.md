# Simulação de Índice Hash Estático com Django e Python

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/-Django-darkgreen?style=flat-square&logo=django)
![Database](https://img.shields.io/badge/-Database-black?style=flat-square&logo=mysql)

Este projeto é uma implementação de um índice hash estático usando Python e Django.

## :dart: Objetivo

Implementar uma interface gráfica ilustrando as estruturas de dados e o funcionamento de um índice hash estático.

## :gear: Funcionalidades Principais

- Construção do índice
- Busca por uma tupla a partir da entrada de uma chave de busca usando o índice construído
- Realizar um table scan dos X primeiras tuplas

## :wrench: Instalação

```bash
git clone https://github.com/tiagoAry15/django-hash-index.git
cd django-hash-index
pip install -r requirements.txt
python manage.py runserver
Depois disso, visite http://localhost:8000/polls no seu navegador.
```
## :book: Uso
- Carregue o arquivo de dados em memória
- Cada linha do arquivo deve gerar uma tupla, que será adicionada à tabela
- As tuplas da tabela devem ser divididas em páginas, de acordo com o tamanho das páginas
 NB buckets de tamanho FR são criados
- A função hash é aplicada à chave de busca de cada tupla
- A chave de busca e o endereço da página onde a tupla foi armazenada são adicionadas ao bucket cujo endereço foi calculado pela função hash
## :handshake: Contribuindo
Contribuições, problemas e solicitações de recursos são bem-vindos! Sinta-se à vontade para verificar issues page.

Se você tem alguma dúvida, sinta-se à vontade para me contatar...
## Demonstração da tela inicial
![Screenshot do Projeto](./screenshot.png)



