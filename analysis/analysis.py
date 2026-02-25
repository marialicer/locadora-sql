# %%
# IMPORTAÇÕES
import pandas as pd
import matplotlib.pyplot as plt
import locale

# %%
# LEITURA DOS DADOS

locacao_dados = pd.read_excel(
    "C:/Users/alice/OneDrive/Documentos/locadora-sql/data/dataset_locadora.xlsx"
)

# %%
# TRATAMENTO DE DATAS

locacao_dados["DATALOC"] = pd.to_datetime(
    locacao_dados["DATALOC"],
    format="%m/%d/%Y"
)

locacao_dados["DATADEVOLUCAO"] = pd.to_datetime(
    locacao_dados["DATADEVOLUCAO"],
    format="%m/%d/%Y"
)

# Criando mês numérico (base para ordenação)
locacao_dados["MES_NUM"] = locacao_dados["DATALOC"].dt.month

# Criando nome do mês apenas para exibição
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
locacao_dados["MES"] = locacao_dados["DATALOC"].dt.strftime("%B")

# %%
# DEMANDA 1 – RECEITA MENSAL
# Entender a evolução da receita

total_por_mes = (
    locacao_dados
    .groupby("MES_NUM")["VALOR"]
    .sum()
    .reset_index()
    .sort_values("MES_NUM")
)

plt.figure(figsize=(10,5))
plt.plot(total_por_mes["MES_NUM"], total_por_mes["VALOR"])
plt.xlabel("Mês")
plt.ylabel("Total Faturado")
plt.title("Receita Mensal")
plt.xticks(total_por_mes["MES_NUM"])
plt.show()

# %%
# DEMANDA 2 – FILMES MAIS RENTÁVEIS
# Quais filmes geram mais dinheiro?

total_filme = (
    locacao_dados
    .groupby("NOMEFILME")["VALOR"]
    .sum()
    .reset_index()
    .sort_values("VALOR", ascending=False)
)

plt.figure(figsize=(12,6))
barras = plt.bar(total_filme["NOMEFILME"], total_filme["VALOR"])

plt.xlabel("Filme")
plt.ylabel("Receita Total")
plt.title("Filmes Mais Rentáveis")
plt.xticks(rotation=0)

for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{altura:.0f}",
        ha="center",
        va="bottom"
    )

plt.show()

# %%
# DEMANDA 3 – CLIENTES MAIS ATIVOS
# Identificar clientes estratégicos

clientes_ativos = (
    locacao_dados
    .groupby("NOMCLIENTE")
    .size()
    .reset_index(name="QUANTIDADE_LOCACOES")
    .sort_values("QUANTIDADE_LOCACOES", ascending=False)
)

plt.figure(figsize=(10,6))
plt.hist(clientes_ativos["QUANTIDADE_LOCACOES"], bins=10)

plt.xlabel("Quantidade de Locações")
plt.ylabel("Número de Clientes")
plt.title("Distribuição de Locações por Cliente")

plt.show()

# %%
# DEMANDA 4 – TAXA DE DEVOLUÇÃO
# Identificar atrasos na devolução

locacao_dados["DEVOLUCAO"] = locacao_dados["DATADEVOLUCAO"].apply(
    lambda x: "Não devolvido" if pd.isna(x) else "Devolvido"
)

taxa_devolucao = locacao_dados["DEVOLUCAO"].value_counts()
total = taxa_devolucao.sum()
percentual = (taxa_devolucao / total) * 100

plt.figure(figsize=(8,5))
barras = plt.bar(taxa_devolucao.index, taxa_devolucao.values)

plt.xlabel("Situação da Devolução")
plt.ylabel("Quantidade")
plt.title("Taxa de Devolução")

for i, barra in enumerate(barras):
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f"{altura:.0f} ({percentual.iloc[i]:.1f}%)",
        ha="center",
        va="bottom"
    )

plt.show()

# %%
# DEMANDA 5 – ANÁLISE TEMPORAL
# Existe sazonalidade?
# Analisar volume de locações por mês
# Verificar tendência de crescimento
# Identificar padrões

locacao_mes = (
    locacao_dados
    .groupby("MES_NUM")
    .size()
    .reset_index(name="TOTAL_LOCACOES")
    .sort_values("MES_NUM")
)

plt.figure(figsize=(10,5))
plt.plot(locacao_mes["MES_NUM"], locacao_mes["TOTAL_LOCACOES"])

plt.xlabel("Mês")
plt.ylabel("Volume de Locações")
plt.title("Volume de Locações por Mês")
plt.xticks(locacao_mes["MES_NUM"])

plt.show()
