# %%
import pandas as pd
import numpy as np
import locale
#%%
locacao_dados = pd.read_csv ("C:/Users/alice/OneDrive/Documentos/locadora-sql/data/locadora_dataset.csv")
# %%
locacao_dados.head()
# %%
from datetime import datetime, date, timedelta
# %%
# Tratamento da variável DATALOC

locacao_dados["DATALOC"] = pd.to_datetime(
    locacao_dados["DATALOC"],
    format = "%m/%d/%Y"
)
# %%
locacao_dados["DATADEVOLUCAO"] = pd.to_datetime(
    locacao_dados["DATADEVOLUCAO"],
    format = "%m/%d/%Y"
)
# %%
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
locacao_dados["MES"] = locacao_dados["DATALOC"].dt.month_name()
locacao_dados["MES"] = locacao_dados["DATALOC"].dt.strftime("%B")
locacao_dados["MES"] = locacao_dados["MES"].replace("marÃ§o", "março")
locacao_dados.head()
# %%

# DEMANDA 1 - RECEITA MENSAL
# Entender a evolução da receita

total_preco = locacao_dados["PRECO"].sum()
print(total_preco)
# %%
total_por_mes = (
    locacao_dados
    .groupby("MES")["PRECO"]
    .sum()
    .reset_index()
)
# %%
ordem_meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

total_por_mes["MES"] = pd.Categorical(
    total_por_mes["MES"],
    categories=ordem_meses,
    ordered=True
)

total_por_mes = total_por_mes.sort_values("MES")
# %%
import matplotlib.pyplot as plt

plt.figure()
plt.plot(total_por_mes["MES"], total_por_mes["PRECO"])
plt.xlabel("Mês")
plt.ylabel("Total Faturado")
plt.title("Receita Mensal")
plt.xticks(rotation=45)
plt.show()
# %%

## Conclusão Receita Mensal: Mês de maior vendas
## foi o mês de março, com um faturamento próximo R$ 180.
## Em maio há uma queda, ficando abaixo do patamar de R$ 140.
## Apesar do baixo desempenho do mês anterior, junho se recupera e chega ao valor de R$ 140.

#%% 
locacao_dados.head()
# %%
# DEMANDA 2 – Filmes Mais Rentáveis
# Quais filmes geram mais dinheiro?

total_filme = (
    locacao_dados
    .groupby("NOMEFILME")["PRECO"]
    .sum()
    .reset_index()
)
total_filme.head()
# %%
total_filme = total_filme.sort_values("PRECO",ascending=False)

# %%
plt.figure(figsize=(12,6))
barras = plt.bar(total_filme['NOMEFILME'],total_filme['PRECO'], color='skyblue')
plt.xlabel('FILME')
plt.ylabel('RENDA POR FILME')
plt.title('FILMES MAIS RENTÁVEIS')
plt.xticks(rotation=0)

for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f'{altura:.0f}',
        ha='center',
        va='bottom'
    )

plt.show()
# %%

## Conclusão Filmes mais rentáveis:
## O filme mais rentável da locadora é o título "As Branquelas".
## A produção gerou receita total de R$ 215.

# %%
locacao_dados.head()
# %%
# DEMANDA 3 – Clientes Mais Ativos
# Identificar clientes estratégicos

clientes_ativos = (
    locacao_dados
    .groupby("NOMCLIENTE")["NOMEFILME"]
    .count()
    .reset_index()
)
clientes_ativos = clientes_ativos.rename(columns={"NOMEFILME": "QUANTIDADE_FILMES"})
clientes_ativos = clientes_ativos.sort_values("QUANTIDADE_FILMES",ascending=False)
# %%
top10_clientes = clientes_ativos.head(10)
top10_clientes
# %%
plt.figure(figsize=(10,6))

plt.hist(clientes_ativos["QUANTIDADE_FILMES"], bins=10)

plt.xlabel("Quantidade de Locações")
plt.ylabel("Número de Clientes")
plt.title("Distribuição de Locações por Cliente")

plt.show()
# %%
clientes_ativos["QUANTIDADE_FILMES"].describe()
# %%
## A base apresenta comportamento relativamente distribuído. 
## A maioria dos clientes realiza entre 3 e 5 locações, 
## sem concentração excessiva em poucos clientes.