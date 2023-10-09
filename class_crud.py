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
        
    def buscar_nome(self,opcao_pesquisa,busca):
        pesquisa = f'SELECT * FROM estoque WHERE {opcao_pesquisa} = "{busca}";'
        self.cursor.execute(pesquisa)

        result = self.cursor.fetchall()
        
        colunas = [desc[0] for desc in self.cursor.description]

        df = pd.DataFrame(result, columns=colunas)
        return df
    
    def fechar(self):
        self.cursor.close()
        self.conexao.close()

    def listarTudo(self):
        self.cursor.execute("select * from estoque;")
        result = self.cursor.fetchall()
        colunas = [desc[0] for desc in self.cursor.description]
        
        df = pd.DataFrame(result,columns=colunas)
        return df
        
    def remover(self,opcao_remove,remove):
        if type(remove) == "float":
            comando = f'DELETE  FROM estoque WHERE {opcao_remove} = {remove};'
        else:
            comando = f'DELETE  FROM estoque WHERE {opcao_remove} = "{remove}";'

        self.cursor.execute(comando)
        self.conexao.commit()

    # def exibiir_produto(self,opcao_exibir):
    #     self.cursor.execute(f'SELECT * FROM estoque WHERE ID_Produto= "{opcao_exibir}";')
    #     result = self.cursor.fetchall()
    #     if result:
    #         colunas = [desc[0] for desc in self.cursor.description]

    #         df = pd.DataFrame(result, columns=colunas)

    #         # Exiba o DataFrame
    #         print(df)
    #     else:
    #         print("Nenhum resultado encontrado.")