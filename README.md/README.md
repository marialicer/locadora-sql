# Sistema de Locadora - Projeto SQL



Projeto desenvolvido em Oracle SQL com foco em modelagem relacional, consultas analíticas, criação de views e triggers para automatização de regras de negócio.



---



## Modelo de Dados



O sistema é composto por 5 tabelas principais:



- CLIENTE

- FILME

- GENERO

- PRECO

- LOCACAO



### Relacionamentos



- Um CLIENTE pode realizar várias LOCAÇÕES (1:N)

- Um FILME pertence a um GÊNERO

- O preço do filme é definido pela COR

- Uma LOCAÇÃO relaciona CLIENTE e FILME



---



## Estrutura das Tabelas



### CLIENTE

Armazena informações dos clientes.



- CODCLIENTE (PK)

- NOMCLIENTE

- ENDCLIENTE

- BAIRCLIENTE

- CIDCLIENTE

- UFCLIENTE



### FILME

Armazena os filmes disponíveis para locação.



- CODFILME (PK)

- NOMEFILME

- COR (FK >> PRECO)

- STATUS (D = Disponível / L = Locado)

- CODGENERO (FK >> GENERO)



### GENERO

Categorias dos filmes.



- CODGENERO (PK)

- DESCRICAO



### PRECO

Define o valor da locação por cor do filme.



- COR (PK)

- VALOR



### LOCACAO

Registra as locações realizadas.



- CODLOCACAO (PK >> Identity)

- CODCLIENTE (FK >> CLIENTE)

- CODFILME (FK >> FILME)

- DATALOC

- DATADEVOLUCAO



---



## Consultas Desenvolvidas



### Listagem de Filmes com Gênero

JOIN entre FILME e GENERO.



### Locações com Nome do Cliente e Filme

JOIN entre CLIENTE, LOCACAO e FILME.



### Filmes Locados

Filtro por STATUS = 'L'.



### Clientes que nunca alugaram

Uso de LEFT JOIN com verificação de NULL.



### Quantidade de Filmes por Cliente

Uso de COUNT() e GROUP BY.



### Total Gasto por Cliente

Uso de SUM() com múltiplos JOINs.



### Filme Mais Alugado

Uso de COUNT() + ORDER BY + FETCH FIRST 1 ROW ONLY.



### Clientes que gastaram mais que 10 reais

Uso de HAVING com agregação.



### Clientes acima da média

Subquery com cálculo de média geral.



---



## View Criada



### CLIENTES\_ACIMA\_DA\_MEDIA



View que retorna clientes cujo total gasto é superior à média geral de gastos.



---



## Automação com Triggers



### TRG_LOCACAO_FILME

Ao inserir uma nova locação:

- Atualiza automaticamente o STATUS do filme para 'L'.



### TRG\_DEVOLUCAO\_FILME

Ao atualizar DATADEVOLUCAO:

- Atualiza automaticamente o STATUS para 'D'.



---



## Tecnologias Utilizadas



- Oracle Database (via Oracle APEX - ambiente cloud)

- PL/SQL (Triggers)

- Git \& GitHub



---



## Conceitos Aplicados



- Modelagem relacional

- Chaves primárias e estrangeiras

- JOIN (INNER e LEFT)

- Funções de agregação

- Subqueries

- Views

- Triggers

- Regras de negócio automatizadas



---


## Objetivo do Projeto



Praticar modelagem de banco de dados relacional e consultas SQL avançadas, aplicando regras de negócio reais em um sistema de locadora.



---





