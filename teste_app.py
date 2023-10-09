# Instancie a classe CRUD
import streamlit as st
from class_crud import CRUD
import pandas as pd

crud = CRUD()

st.title("Gerenciamento do estoque")

# Escolha a operação CRUD
operacao = st.selectbox("Selecione a operação:", ["Inserir", "Alterar", "Buscar", "Listar", "Remover"])

if operacao == "Inserir":
    st.subheader("Inserir Registro")
    nome = st.text_input("Nome")
    tipo = st.text_input("Tipo")
    fornecedor = st.text_input("Fornecedor")
    peso = st.number_input("Peso")
    
    if st.button("Inserir"):
        crud.inserir(nome, tipo, fornecedor, peso)
        
elif operacao == "Alterar":
    st.subheader("Aterar Registro")
    coluna = st.selectbox("Selecione a coluna para alterar:", ["Nome", "Tipo", "Fornecedor", "Peso"])
    alteracao = st.text_input(f"Nova {coluna}")
    onde = st.number_input("ID do Registro")
    
    if st.button("Alterar"):
        crud.alterar(coluna, alteracao, onde)

elif operacao == "Buscar":
    st.subheader("Buscar Produto(s)")
    opcao_pesquisa = st.selectbox("Selecione a opção de pesquisa:", ["Nome", "Tipo", "Fornecedor"])
    
    busca = st.text_input("Digite o que busca")
    if st.button("Buscar"):
        result = crud.buscar_nome(opcao_pesquisa,busca)
       
        if result is not None and not result.empty:
            st.table(result)
        else:
            st.write("Nenhum resultado encontrado.")

elif operacao == "Listar":
    st.subheader("Listar Registros")
    result = crud.listarTudo()
    
    if result is not None and not result.empty:
        st.table(result)
    else:
        st.write("Nenhum resultado encontrado.")

elif operacao == "Remover":
    st.subheader("Remover Registro")
    opcao_remove = st.selectbox("Selecione a opção de remoção:", ["ID_Produto", "Nome", "Tipo", "Fornecedor"])

    if opcao_remove == "ID_Produto":
        remove = st.number_input("Digite o que deseja remover")
    else:
        remove = st.text_input("Digite o que deseja remover")

    if st.button("Remover"):
        crud.remover(opcao_remove,remove)

# Feche a conexão com o banco de dados no final
crud.fechar()