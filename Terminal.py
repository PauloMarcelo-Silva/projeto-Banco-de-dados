from class_crud import CRUD
import pandas as pd
import os 


print("---------------- Bem Vindo ao Estoque-----------------")

while(True):
    opcao = int(input("""Menu:
                opção 1 = Adicionar
                opçao 2 = alterar
                opçao 3 = Pesquisar
                Opção 4 = Visualizar itens na lista
                Opção 5 = Remover
                Opção 6 = Exibir um produto \n""""Digite uma opção: "))
                
    if opcao == 1:
        nome = str(input("Digite o nome do produto: "))
        tipo = str(input("Digite o tipo do produto: "))
        fornecedor = str(input("Digite o fornecedor do produto: "))
        peso = float(input("Digite o peso do produto: "))
        crud = CRUD()
        crud.inserir(nome,tipo,fornecedor,peso)
        crud.fechar()
        os.system('cls')

    elif opcao == 2:
        coluna = [None,'Nome','Tipo','Fornecedor','Peso']
        os.system('cls')
        print("""Oque vc deseja alterar?
                        Nome = 1
                        Tipo = 2
                        Fornecedor = 3
                        Peso = 4\n""")
        coluna_alt = int(input("Digite a opção: "))
        onde = int(input("Digite o ID do profuto: "))
        alteracao = str(input("Digite a alteração: "))
        
        
        crud = CRUD()
        
        crud.alterar(coluna[coluna_alt],alteracao,onde)
        os.system('cls')

    elif opcao == 3:
        os.system('cls')
        print("""Por qual opção você deseja pesquisar:
                                1 = Nome
                                2 = Tipo
                                3 = Fornecedor\n""")
        opcao_pesquisa = int(input("Digte a opcao: "))
        
        crud = CRUD()
        
        crud.buscar_nome(opcao_pesquisa)
        input("\n\nDigite qualuqer tecla para voltar ao menu.")
        os.system('cls')

        
    elif opcao == 4:
        os.system('cls')
        crud = CRUD()
        crud.listarTudo()
        input("\n\nDigite qualuqer tecla para voltar ao menu.")
        os.system('cls')

    elif opcao == 5:
        os.system('cls')
        print("""Por qual opção você deseja remover:
                                1 = ID
                                2 = Nome
                                3 = Tipo
                                4 = Fornecedor\n""")
        opcao_remove = int(input("Digite a opção: "))
        crud = CRUD()
        crud.remover(opcao_remove)
        os.system('cls')
        
    elif opcao == 6 :
        opcao_exibir= int(input("Digite o codigo do produto:"))
        os.system('cls')
        crud= CRUD()
        crud.exibiir_produto(opcao_exibir)
        input("\n\nDigite qualuqer tecla para voltar ao menu.")