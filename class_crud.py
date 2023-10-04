import mysql.connector
import pandas as pd
import os
class CRUD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='159357123',
            database='empresa_queijos',
        )
        self.cursor = self.conexao.cursor()
        
    def inserir(self,nome,tipo,fornecedor,peso):
        preco = 0

        if tipo == "Queijo":
            preco = peso * 58.20
        else:
            preco = peso * 24.50
    
        
        comando_adicionar = f'INSERT INTO Estoque (Nome, Tipo, Fornecedor, Peso, Preço) VALUES ("{nome}", "{tipo}", "{fornecedor}", {peso}, {preco});'
        self.cursor.execute(comando_adicionar)
        self.conexao.commit()
        
    def alterar(self,coluna,alteracao,onde):
        comando_alterar = f'UPDATE estoque SET {coluna} = "{alteracao}" WHERE ID_Produto = {onde}'
        self.cursor.execute(comando_alterar)
        self.conexao.commit()
        
    def buscar_nome(self,opcao_pesquisa,):
        if opcao_pesquisa == 1:
            pesquisa_nome = str(input("Digite o nome que você deseja pesquisar: "))
            opcao_pesquisa = f'SELECT * FROM estoque WHERE Nome = "{pesquisa_nome}";'
        elif opcao_pesquisa == 2:
            pesquisa_Tipo = str(input("Digite o tipo do produto que você deseja pesquisar: "))
            opcao_pesquisa= f'SELECT * FROM estoque WHERE Tipo = "{pesquisa_Tipo}";'
        elif opcao_pesquisa == 3:
            pesquisa_Fornecedor = str(input("Digite os produtos do fornecedor que você deseja pesquisar: "))
            opcao_pesquisa = f'SELECT * FROM estoque WHERE Fornecedor = "{pesquisa_Fornecedor}";'
        os.system('cls')
        self.cursor.execute(opcao_pesquisa)

        result = self.cursor.fetchall()
        if result:
            colunas = [desc[0] for desc in self.cursor.description]

            df = pd.DataFrame(result, columns=colunas)

            # Exiba o DataFrame
            print(df)
        else:
            print("Nenhum resultado encontrado.")
        
    def listar_tudo(self,comando):
        self.cursor.execute(comando)
        result = self.cursor.fetchall()
        return result
    
    def exibir_um(self,comando):
        self.cursor.execute(comando)
        
    def deletar(self,comando):
        self.cursor.execute(comando)
        self.conexao.commit()
        
    def fechar(self):
        self.cursor.close()
        self.conexao.close()

    def listarTudo(self):
        self.cursor.execute("select * from estoque;")
        result = self.cursor.fetchall()

        # Verifique se há algum resultado
        if result:
            # Recupere os nomes das colunas
            colunas = [desc[0] for desc in self.cursor.description]

            # Crie um DataFrame Pandas com os resultados e nomes das colunas
            df = pd.DataFrame(result, columns=colunas)

            # Exiba o DataFrame
            print(df)
        else:
            print("Nenhum resultado encontrado.")
    
    def remover(self,opcao_remove):
        if opcao_remove == 1:
            remove_nome = str(input("Digite o ID do produto que você deseja remover: "))
            remover = f'DELETE FROM estoque WHERE ID_Produto = "{remove_nome}";'
        elif opcao_remove == 2:
            remove_nome = str(input("Digite o nome que você deseja remover: "))
            remover = f'DELETE FROM estoque WHERE Nome = "{remove_nome}";'
        elif opcao_remove == 3:
            remove_Tipo = str(input("Digite o tipo do produto que você deseja remover: "))
            remover= f'DELETE  FROM estoque WHERE Tipo = "{remove_Tipo}";'
        elif opcao_remove == 3:
            remove_Fornecedor = str(input("Digite os produtos do fornecedor que você deseja remover: "))
            remover = f'DELETE  FROM estoque WHERE Fornecedor = "{remove_Fornecedor}";'
        
        self.cursor.execute(remover)
        self.conexao.commit()

    def exibiir_produto(self,opcao_exibir):
        self.cursor.execute(f'SELECT * FROM estoque WHERE ID_Produto= "{opcao_exibir}";')
        result = self.cursor.fetchall()
        if result:
            colunas = [desc[0] for desc in self.cursor.description]

            df = pd.DataFrame(result, columns=colunas)

            # Exiba o DataFrame
            print(df)
        else:
            print("Nenhum resultado encontrado.")