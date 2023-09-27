import mysql.connector
import pandas as pd

class CRUD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='homenverde1',
            database='empresa_queijos',
        )
        self.cursor = self.conexao.cursor()
        
    def inserir(self,comando):
        self.cursor.execute(comando)
        self.conexao.commit()
        
    def alterar(self,comando):
        self.cursor.execute(comando)
        self.conexao.commit()
        
    def buscar_nome(self,comando):
        self.cursor.execute(comando)
        
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

    def pandas_print(self):
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