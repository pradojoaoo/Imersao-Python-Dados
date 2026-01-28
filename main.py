import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')
print(df.head(10))
df.info()
df.describe()
df.shape
linhas, colunas = df.shape[0], df.shape[1]
print('Linhas:', linhas)
print('Colunas:', colunas)
df.columns
renomear_colkunas = {
    'work_year': 'Ano',
    'experience_level': 'Senioridade',
    'employment_type': 'Contrato',
    'job_title': 'Cargo',
    'salary': 'Salario',
    'salary_currency': 'Moeda',
    'salary_in_usd': 'Usd',
    'employee_residence': 'Residencia',
    'remote_ratio': 'Remoto',
    'company_location': 'Empresa',
    'company_size': 'Tamanho_empresa'
}
df.rename(columns=renomear_colkunas, inplace=True)
df.columns
df["Senioridade"].value_counts()
df["Contrato"].value_counts()
df["Remoto"].value_counts()
df["Tamanho_empresa"].value_counts()

Senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df['Senioridade'] = df['Senioridade'].replace(Senioridade)
df["Senioridade"].value_counts()
Contrato = {
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer'
}
df['Contrato'] = df['Contrato'].replace(Contrato)
df["Contrato"].value_counts()

Tamango_empresa = {
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
}
df['Tamanho_empresa'] = df['Tamanho_empresa'].replace(Tamango_empresa)  
df["Tamanho_empresa"].value_counts()

Remoto = {
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
}

df['Remoto'] = df['Remoto'].replace(Remoto)
df["Remoto"].value_counts()
df.head()
df.describe(include=['object', 'string'])
print(df.describe(include=['object', 'string']))
print(df.info())