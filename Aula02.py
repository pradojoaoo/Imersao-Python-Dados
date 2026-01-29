import main

df = main.carregar_e_processar_dados()

print(df.isnull().sum())

df.isnull().sum()

print(df['Ano'].unique())

print(df[df.isnull().any(axis=1)])

import numpy as np # Importando a biblioteca numpy
import pandas as pd # Importando a biblioteca pandas

df_salarios = pd.DataFrame({ # Criando DataFrame de exemplo com valores NaN = NULLO
    "Nome": ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    "Salarios": [4000, np.nan, 5000, np.nan, 100000]
})

df_salarios["Salario_media"] = df_salarios["Salarios"].fillna(df_salarios["Salarios"].mean().round(2)) # Preenchendo valores NaN com a média arredondada para 2 casas decimais
df_salarios["Salario_mediana"] = df_salarios["Salarios"].fillna(df_salarios["Salarios"].median()) # Preenchendo valores NaN com a mediana e deixa melhor para valores extremos
print(df_salarios)

df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})
print("\n")

df_temperaturas["Preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()  # Preenchendo valores NaN com o valor anterior (forward fill)
print(df_temperaturas) 
print("\n")

df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["Preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()  # Preenchendo valores NaN com o valor seguinte (backward fill)
print(df_temperaturas) 
print("\n")

df_cidades = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    "Cidade": ["Sao Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

df_cidades["Cidade_Preenchida"] = df_cidades["Cidade"].fillna("Não Informado") # Preenchendo valores NaN com um valor fixo
print(df_cidades)
print("\n")

df_limpo = df.dropna() # Removendo linhas com valores NaN
df_limpo.isnull().sum()
print(df_limpo.isnull().sum())

df_limpo.head()
print(df_limpo.head())

df_limpo.info()
print(df_limpo.info())

df_limpo = df_limpo.assign(Ano = df_limpo["Ano"].astype("int64")) # Convertendo a coluna 'Ano' para o tipo inteiro
print(df_limpo.head())