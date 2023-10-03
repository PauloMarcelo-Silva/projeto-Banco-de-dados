from class_crud import CRUD
import pandas as pd
import os 


print("---------------- Bem Vindo ao Estoque-----------------")

while(True):
    opcao = int(input("""Digite a opção:
                opção 1 = Adicionar
                opçao 2 = alterar
                opçao 3 = Pesquisar
                Opção 4 = Visualizar itens na lista.\n"""))
    if opcao == 1:
        nome = str(input("Digite o nome do produto: "))
        tipo = str(input("Digite o tipo do produto: "))
        fornecedor = str(input("Digite o fornecedor do produto: "))
        peso = float(input("Digite o peso do produto: "))
        preco = 0

        if tipo == "Queijo":
            preco = peso * 58.20
        else:
            preco = peso * 24.50
    
        crud = CRUD()
        comando_adicionar = f'INSERT INTO Estoque (Nome, Tipo, Fornecedor, Peso, Preço) VALUES ("{nome}", "{tipo}", "{fornecedor}", {peso}, {preco});'
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
        opcao_pesquisa = int(input("""Por qual opção você deseja pesquisar:
                                1 = Nome
                                2 = Tipo
                                3 = Fornecedor\n"""))
        crud = CRUD()
        if opcao_pesquisa == 1:
            pesquisa_nome = str(input("Digite o nome que você deseja pesquisar: "))
            opcao_pesquisa = f'SELECT * FROM estoque WHERE Nome = "{pesquisa_nome}";'
        elif opcao_pesquisa == 2:
            pesquisa_Tipo = str(input("Digite o tipo do produto que você deseja pesquisar: "))
            opcao_pesquisa= f'SELECT * FROM estoque WHERE Tipo = "{pesquisa_Tipo}";'
        elif opcao_pesquisa == 3:
            pesquisa_Fornecedor = str(input("Digite os produtos do fornecedor que você deseja pesquisar: "))
            opcao_pesquisa = f'SELECT * FROM estoque WHERE Fornecedor = "{pesquisa_Fornecedor}";'
        crud.buscar_nome(opcao_pesquisa)
        
    elif opcao == 4:
        crud = CRUD()
        crud.pandas_print()
        print("apareceu")

