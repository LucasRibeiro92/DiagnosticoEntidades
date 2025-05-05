import os
import pandas as pd
import psycopg2

# === CONFIGURAÇÕES DO BANCO ===
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'diagnosticoentidades'
DB_USER = 'postgres'
DB_PASS = '231224'

# === CONEXÃO COM O POSTGRES ===
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

# === LÊ OS DADOS COM SELECT ===
query = "SELECT * FROM execucoes"
df = pd.read_sql_query(query, conn)

# === GARANTE A PASTA 'processed/' ===
output_dir = 'C:/PythonProjects/diagnosticoentidades/data/processed'
os.makedirs(output_dir, exist_ok=True)

# === SALVA COMO CSV ===
output_path = os.path.join(output_dir, 'execucoes_exportadas.csv')
df.to_csv(output_path, index=False)

# === FINALIZA ===
conn.close()
print(f"✅ Dados exportados para {output_path}")