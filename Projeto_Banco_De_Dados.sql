USE empresa_queijos;
create table Estoque(
ID_Produto int(50) NOT NULL,
Nome varchar(50) NOT NULL,
Tipo varchar(50) NOT NULL,
Fornecedor varchar(50),
Peso float(50) NOT NULL,
Preço float(50) NOT NULL,
PRIMARY KEY (ID_Produto)
);



