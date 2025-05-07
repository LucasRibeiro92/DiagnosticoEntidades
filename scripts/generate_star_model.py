import pandas as pd

# === 1. Carregar os dados da pasta correta ===
df = pd.read_csv('C:/PythonProjects/diagnosticoentidades/data/processed/execucoes_exportadas.csv')  # ajuste conforme o nome real do seu arquivo

# Garantir que a coluna de data esteja como datetime
df['data_execucao'] = pd.to_datetime(df['data_execucao'])

# === 2. Criar Dimensão Entidade ===
dim_entidade = df[['nome_entidade']].drop_duplicates().reset_index(drop=True)
dim_entidade['id_entidade'] = dim_entidade.index + 1

# === 3. Criar Dimensão Servidor ===
dim_servidor = df[['servidor']].drop_duplicates().reset_index(drop=True)
dim_servidor['id_servidor'] = dim_servidor.index + 1

# === 4. Criar Dimensão Categoria ===
dim_categoria = df[['categoria_entidade']].drop_duplicates().reset_index(drop=True)
dim_categoria['id_categoria'] = dim_categoria.index + 1

# === 5. Criar Dimensão Tempo ===
dim_tempo = df[['data_execucao']].drop_duplicates().reset_index(drop=True)
dim_tempo['id_tempo'] = dim_tempo.index + 1
dim_tempo['ano'] = dim_tempo['data_execucao'].dt.year
dim_tempo['mes'] = dim_tempo['data_execucao'].dt.month
dim_tempo['dia'] = dim_tempo['data_execucao'].dt.day
dim_tempo['dia_semana'] = dim_tempo['data_execucao'].dt.day_name()
dim_tempo['hora'] = dim_tempo['data_execucao'].dt.hour

# === 6. Criar Fato Execuções ===
fato = df.merge(dim_entidade, on='nome_entidade') \
         .merge(dim_servidor, on='servidor') \
         .merge(dim_categoria, on='categoria_entidade') \
         .merge(dim_tempo, on='data_execucao')

fato_execucoes = fato[['id_execucao', 'id_entidade', 'id_servidor', 'id_categoria', 'id_tempo',
                       'tempo_execucao_seg', 'status_execucao']]

# Tempo médio esperado por entidade
fato_execucoes['tempo_medio_esperado'] = fato_execucoes.groupby('id_entidade')['tempo_execucao_seg'].transform('mean').round().astype(int)

# Desvio de execução
fato_execucoes['desvio_execucao'] = fato_execucoes['tempo_execucao_seg'] - fato_execucoes['tempo_medio_esperado']

# === 7. Salvar os arquivos normalizados ===
dim_entidade.to_csv('C:/PythonProjects/diagnosticoentidades/data/mart/dim_entidade.csv', index=False)
dim_servidor.to_csv('C:/PythonProjects/diagnosticoentidades/data/mart/dim_servidor.csv', index=False)
dim_categoria.to_csv('C:/PythonProjects/diagnosticoentidades/data/mart/dim_categoria.csv', index=False)
dim_tempo.to_csv('C:/PythonProjects/diagnosticoentidades/data/mart/dim_tempo.csv', index=False)
fato_execucoes.to_csv('C:/PythonProjects/diagnosticoentidades/data/mart/fato_execucoes.csv', index=False)
