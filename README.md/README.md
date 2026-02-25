# Sistema de Locadora – Projeto SQL & Python

Sistema de locadora desenvolvido com Oracle SQL para modelagem relacional e automação de regras de negócio, complementado por análise exploratória em Python para geração de insights estratégicos.

---

## Objetivo do Projeto

Praticar modelagem de banco de dados relacional e consultas SQL avançadas, aplicando regras de negócio reais em um sistema de locadora. A análise exploratória com Python possibilitou insights para apoio à tomada de decisão.

---

## Tecnologias Utilizadas

- Oracle Database (Oracle APEX – ambiente cloud)
- PL/SQL (Triggers)
- SQL (consultas avançadas)
- Python (análise exploratória)
- Git & GitHub

---

## Estrutura do Projeto

### Modelagem e Banco de Dados
- Modelagem relacional
- Chaves primárias e estrangeiras
- Views para relatórios
- Triggers para automação de regras de negócio

### Análise de Dados
- Exploração e visualização com Python
- Insights estratégicos
- Indicadores de desempenho

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

---

### FILME
Armazena os filmes disponíveis para locação.

- CODFILME (PK)
- NOMEFILME
- COR (FK → PRECO)
- STATUS (D = Disponível / L = Locado)
- CODGENERO (FK → GENERO)

---

### GENERO
Categorias dos filmes.

- CODGENERO (PK)
- DESCRICAO

---

### PRECO
Define o valor da locação por cor do filme.

- COR (PK)
- VALOR

---

### LOCACAO
Registra as locações realizadas.

- CODLOCACAO (PK – Identity)
- CODCLIENTE (FK → CLIENTE)
- CODFILME (FK → FILME)
- DATALOC
- DATADEVOLUCAO

---

## Consultas Desenvolvidas

- Listagem de filmes com gênero (JOIN)
- Locações com cliente e filme (JOIN múltiplo)
- Filmes locados (STATUS = 'L')
- Clientes que nunca alugaram (LEFT JOIN)
- Quantidade de filmes por cliente (COUNT + GROUP BY)
- Total gasto por cliente (SUM + JOIN)
- Filme mais alugado (ORDER BY + LIMIT)
- Clientes que gastaram mais que R$ 10 (HAVING)
- Clientes acima da média (subquery)

---

## Views Criadas

### CLIENTES_ACIMA_DA_MEDIA
View que retorna clientes cujo total gasto é superior à média geral de gastos.

---

## Automação com Triggers

### TRG_LOCACAO_FILME
Ao inserir uma nova locação:

- Atualiza automaticamente o STATUS do filme para 'L'

### TRG_DEVOLUCAO_FILME
Ao atualizar DATADEVOLUCAO:

- Atualiza automaticamente o STATUS para 'D'

---

## Insights da Análise com Python

### Receita Mensal
- Crescimento após queda em maio
- Março e abril apresentaram maior faturamento

### Filmes Mais Rentáveis
- As Branquelas (215 locações)
- Toy Story (195)
- O Exorcista (175)
- Velozes & Furiosos (170)
- Titanic (130)

### Clientes Ativos
- Distribuição entre 1 e 9 locações
- Possibilidade de segmentação (baixo, médio e alto engajamento)

### Taxa de Devolução
- Cerca de 19% dos filmes ainda não foram devolvidos
- Sugere reforço em políticas de devolução

### Sazonalidade
- Março e abril com maior volume de locações
- Pode orientar campanhas e planejamento de estoque