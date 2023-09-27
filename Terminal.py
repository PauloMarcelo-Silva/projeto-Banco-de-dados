from class_crud import CRUD
import pandas as pd
import os 


print("---------------- Bem Vindo ao Estoque-----------------")

while(True):
    opcao = int(input("""Digite a opção:
                opção 1 = Adicionar
                opçao 2 = alterar
                Opção 3 = Visualizar itens na lista.\n"""))
    if opcao == 1:
        id = int(input("Digite o id do produto: "))
        nome = str(input("Digite o nome do produto: "))
        tipo = str(input("Digite o tipo do produto: "))
        fonecedor = str(input("Digite o fornecedor do produto: "))
        peso = float(input("Digite o peso do produto: "))
        preço = 0

        if tipo == "Queijo":
            preço = peso * 58.20
        else:
            preço = peso * 24,50
        
        crud = CRUD()
        comando_adicionar = f'insert into estoque values ({id},"{nome}","{tipo}","{fonecedor}",{peso},{preço});'
        crud.inserir(comando_adicionar)
        crud.fechar()
        os.system('cls')
    elif opcao == 2:
        coluna = [None,'Nome','Tipo','Fornecedor','Peso']
        coluna_alt = int(input("""Oque vc deseja alterar?
                        Nome = 1
                        Tipo = 2
                        Fornecedor = 3
                        Peso = 4\n"""))
        alteracao = str(input("Qual seria a alteração? \n "))
        oque = int(input("Qual Id do produto? \n"))
        
        crud = CRUD()
        comando_alterar = f'UPDATE estoque SET {coluna[coluna_alt]} = "{alteracao}" WHERE ID_Produto = {oque}'
        crud.alterar(comando_alterar)
        os.system('cls')
    elif opcao == 3:
        crud = CRUD()
        crud.pandas_print()
        print("apareceu")

