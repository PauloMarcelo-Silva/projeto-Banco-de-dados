# Sistema de Gestão de Vendas e Estoque para Distribuidora de Queijos

## Introdução

Este projeto foi desenvolvido com o objetivo de criar um sistema de gestão de vendas e estoque para uma distribuidora de queijos. A aplicação permite gerenciar o estoque de queijos, cadastrar fornecedores, clientes e realizar vendas. O sistema oferece funcionalidades de inserção, alteração, pesquisa, remoção e listagem de dados, além de um módulo completo de vendas.

## Temas Disponíveis

Embora este projeto seja específico para uma distribuidora de queijos, ele pode ser adaptado para outros temas, como:

1. Supermercado
2. Mercado
3. Banca de Revista
4. Lanchonete
5. Doceria
6. Churrascaria
7. Churrasquinho
8. Sanduicheria
9. Restaurante
10. Bar
11. Quentinha/Marmita
12. Material de Construção
13. Construtora
14. Consultório
15. Clínica
16. Livraria
17. Outros

## Especificações do Sistema

### Parte 1 - Sistema CRUD

1. **Funcionalidades CRUD:**
    - Inserir
    - Alterar
    - Pesquisar por nome
    - Remover
    - Listar todos
    - Exibir um

2. **Modelagem UML:**
    - Diagrama UML das classes utilizadas no sistema.

3. **Gerenciamento de Operações CRUD:**
    - Classe que gerencia as operações CRUD.

4. **Objetos com Múltiplos Atributos:**
    - Objeto principal (ex: Produto) com pelo menos 4 atributos.

5. **Métodos:**
    - Uso extensivo de métodos.

6. **Relatórios:**
    - Geração de relatórios com resumo das informações (quantidade de elementos cadastrados, valor total, etc).

### Parte 2 - Módulo de Vendas

1. **Sistema de Vendas Completo:**
    - Relacionamentos entre clientes, vendedores e compras.
    - Múltiplos itens por compra.
    - Verificação de estoque antes da efetivação de compras.

2. **Funcionalidades Adicionais:**
    - Filtragem de produtos por nome, faixa de preço, categoria e origem.
    - Descontos para clientes específicos (torcedores do Flamengo, fãs de One Piece, ou residentes em Sousa).
    - Relatórios mensais de vendas por vendedor.
    - Verificação de produtos com menos de 5 unidades em estoque.

3. **Banco de Dados:**
    - Uso de views e stored procedures.
    - Implementação de índices e restrições de integridade referencial.

## Implementação

### Tecnologias Utilizadas

- **Plataforma de Desenvolvimento:**
    - Escolha da plataforma de acordo com a familiaridade (console, web, desktop, app).

- **Banco de Dados:**
    - Qualquer SGBD disponível nos laboratórios do CI ou em ambientes de nuvem.

- **Linguagem de Programação:**
    - Qualquer linguagem disponível nos laboratórios do CI ou em ambientes de nuvem.

### Executando o Projeto

1. Clone este repositório.
2. Configure o banco de dados conforme as instruções no arquivo de configuração.
3. Execute os scripts para criar as tabelas e carregar os dados iniciais.
4. Utilize a interface gráfica para interagir com o sistema.
