# Sistema de Locadora - Projeto SQL e Python


Projeto desenvolvido com Oracle SQL para modelagem relacional e automação de regras de negócio, complementado por análise exploratória em Python para geração de insights estratégicos. O trabalho envolveu:

- Modelagem do banco de dados relacional
- Consultas analíticas para avaliação de desempenho
- Criação de views para simplificação de relatórios
- Triggers para automatização de regras de negócio
- Análise exploratória com Python para compreensão dos dados



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

Praticar modelagem de banco de dados relacional e consultas SQL avançadas, aplicando regras de negócio reais em um sistema de locadora. O projeto também inclui análise exploratória com Python, permitindo insights baseados em dados para apoiar decisões estratégicas.


---

## Principais insights da análise exploratória dos dados usando Python

### DEMANDA 1 – Receita Mensal
Contexto:

A diretoria quer entender a evolução da receita.

A receita da locadora apresentou crescimento após uma queda em maio, quando ficou abaixo de R$ 140. Os meses de maior faturamento foram março e abril, indicando possível sazonalidade ou eventos que impulsionaram as locações.

---

### DEMANDA 2 – Filmes Mais Rentáveis
Contexto:

O time quer saber quais filmes geram mais dinheiro.

Os filmes mais rentáveis da locadora são "As Branquelas" (215 locações), "Toy Story" (195), "O Exorcista" (175), "Velozes & Furiosos" (170) e "Titanic" (130)". Esses filmes representam oportunidades para campanhas e promoções estratégicas.

---

### DEMANDA 3 – Clientes Mais Ativos
Contexto:

Marketing quer identificar clientes estratégicos.

Tendência de concentração em torno de 3–5 locações. Não é extremamente concentrada, pois há dispersão (1 a 9). Distribuição moderada, com alguns clientes muito ativos e outros pouco ativos. Isso sugere segmentação possível para marketing (baixo, médio e alto engajamento).

---

### DEMANDA 4 – Taxa de Devolução
Contexto:

Operações quer saber se há atrasos.

O percentual de filmes não devolvidos atualmente está em aproximadamente 19%, com 38 dvd's ainda não sido entregues. Pode indicar necessidade de reforço em políticas de devolução ou comunicação com clientes.

---

### DEMANDA 5 – Análise Temporal
Contexto:

Existe sazonalidade?

Os meses de março e abril costumam apresentar maiores volumes de locação por mês, chegando ao pico de 40 filmes locados em março. Evidência de sazonalidade, útil para planejamento de estoque e campanhas.




