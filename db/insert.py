import pandas as pd
import psycopg2
from psycopg2 import sql

# === CONFIGURAÇÕES DO BANCO ===
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'diagnosticoentidades'
DB_USER = 'postgres'
DB_PASS = '231224'

# === LÊ O CSV ===
csv_path = 'C:/PythonProjects/diagnosticoentidades/data/raw/mocked_data.csv'
df = pd.read_csv(csv_path)

# Renomeia a coluna para bater com a tabela
df.rename(columns={'inicio_execucao': 'data_execucao'}, inplace=True)

# === CONEXÃO COM O POSTGRES ===
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# === INSERÇÃO DOS DADOS ===
for _, row in df.iterrows():
    insert_query = sql.SQL("""
                           INSERT INTO execucoes
                           (id_execucao, nome_entidade, data_execucao, tempo_execucao_seg, status_execucao, servidor,
                            categoria_entidade)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)
                           """)

    cur.execute(insert_query, (
        row['id_execucao'],
        row['nome_entidade'],
        row['data_execucao'],
        int(row['tempo_execucao_seg']),
        row['status_execucao'],
        row['servidor'].lower(),  # Convertendo para lowercase (caso necessário)
        row['categoria_entidade']
    ))

# === COMMIT E FECHAMENTO ===
conn.commit()
cur.close()
conn.close()

print("✅ Dados inseridos com sucesso.")
