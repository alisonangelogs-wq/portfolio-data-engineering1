import pandas as pd
import sqlite3

# caminho dos arquivos
CSV_PATH = "data/employee_times.csv"
DB_PATH = "database/company.db"

print("Lendo arquivo CSV...")
df = pd.read_csv(CSV_PATH)

print("Tratando dados...")

# transformar colunas em datetime
df["date"] = pd.to_datetime(df["date"])
df["check_in"] = pd.to_datetime(df["check_in"], format='%H:%M:%S').dt.time
df["lunch_out"] = pd.to_datetime(df["lunch_out"], format='%H:%M:%S').dt.time
df["lunch_in"] = pd.to_datetime(df["lunch_in"], format='%H:%M:%S').dt.time
df["check_out"] = pd.to_datetime(df["check_out"], format='%H:%M:%S').dt.time

print("Conectando ao banco SQLite...")
conn = sqlite3.connect(DB_PATH)

print("Criando tabela e inserindo dados...")
df.to_sql("employee_times", conn, if_exists="replace", index=False)

conn.close()

print("ETL finalizado com sucesso!")