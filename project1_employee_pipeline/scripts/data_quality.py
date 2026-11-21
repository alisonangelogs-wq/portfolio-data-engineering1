
import sqlite3
import pandas as pd
import sys

DB_PATH = "database/company.db"

print("=" * 55)
print("RELATORIO DE QUALIDADE DOS DADOS")
print("=" * 55)

# Conectar ao banco de dados
conn = sqlite3.connect(DB_PATH)

# Consultar os registros
df = pd.read_sql_query(
    "SELECT * FROM employee_times_staging",
    conn
)

conn.close()

# Verificar se existem dados
if df.empty:
    print("Nenhum registro encontrado.")
    sys.exit(1)

print(f"\nTotal de registros analisados: {len(df)}")

# Campos obrigatórios
required_columns = [
    "employee_id",
    "date",
    "check_in",
    "lunch_out",
    "lunch_in",
    "check_out"
]

# 1. Verificar campos obrigatórios ausentes
missing = df[required_columns].isna().any(axis=1)

print("\n1. Registros com campos obrigatorios ausentes:")
print(missing.sum())

# 2. Verificar registros duplicados
duplicates = df.duplicated(
    subset=["employee_id", "date"],
    keep=False
)

print("\n2. Registros duplicados:")
print(duplicates.sum())

# Converter horários para duração
time_columns = [
    "check_in",
    "lunch_out",
    "lunch_in",
    "check_out"
]

times = {}

for column in time_columns:
    times[column] = pd.to_timedelta(
        df[column],
        errors="coerce"
    )

# 3. Verificar horários inválidos
invalid_times = pd.DataFrame(times).isna().any(axis=1)

print("\n3. Registros com horarios invalidos:")
print(invalid_times.sum())

# 4. Verificar sequência cronológica
valid_times = ~invalid_times

invalid_sequence = (
    valid_times
    & (
        (times["check_in"] >= times["lunch_out"])
        | (times["lunch_out"] >= times["lunch_in"])
        | (times["lunch_in"] >= times["check_out"])
    )
)

print("\n4. Registros com sequencia de horarios invalida:")
print(invalid_sequence.sum())

# 5. Calcular duração da jornada
work_minutes = (
    (times["lunch_out"] - times["check_in"])
    + (times["check_out"] - times["lunch_in"])
)

invalid_duration = (
    valid_times
    & (
        (work_minutes <= pd.Timedelta(0))
        | (work_minutes > pd.Timedelta(hours=24))
    )
)

print("\n5. Registros com duracao invalida:")
print(invalid_duration.sum())

# Resultado geral
total_issues = (
    missing.sum()
    + duplicates.sum()
    + invalid_times.sum()
    + invalid_sequence.sum()
    + invalid_duration.sum()
)

print("\n" + "=" * 55)
print("RESUMO DA VALIDACAO")
print("=" * 55)

print(f"Registros analisados: {len(df)}")
print(f"Ocorrencias identificadas: {total_issues}")

if total_issues == 0:
    print("Resultado: Nenhuma inconsistência identificada.")
else:
    print("Resultado: Foram identificadas inconsistências.")

print("=" * 55)
if total_issues > 0:
    sys.exit(1)
