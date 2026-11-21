import sqlite3

DB_PATH = "database/company.db"

STAGING_TABLE = "employee_times_staging"
PRODUCTION_TABLE = "employee_times"

print("=" * 55)
print("PROMOCAO DOS DADOS PARA PRODUCAO")
print("=" * 55)

conn = sqlite3.connect(DB_PATH)

try:
    cursor = conn.cursor()

    # Verificar se a tabela staging existe
    staging_exists = cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table' AND name = ?
        """,
        (STAGING_TABLE,)
    ).fetchone()

    if staging_exists is None:
        raise Exception("Tabela staging nao encontrada.")

    # Iniciar transacao
    conn.execute("BEGIN IMMEDIATE")

    # Verificar quantidade de registros
    total_records = cursor.execute(
        f"SELECT COUNT(*) FROM {STAGING_TABLE}"
    ).fetchone()[0]

    if total_records == 0:
        raise Exception("Nenhum registro encontrado na staging.")

    # Verificar se a tabela definitiva existe
    production_exists = cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table' AND name = ?
        """,
        (PRODUCTION_TABLE,)
    ).fetchone()

    if production_exists:
        print("Atualizando tabela definitiva...")

        cursor.execute(f"DELETE FROM {PRODUCTION_TABLE}")

        cursor.execute(
            f"""
            INSERT INTO {PRODUCTION_TABLE}
            SELECT * FROM {STAGING_TABLE}
            """
        )
    else:
        print("Criando tabela definitiva...")

        cursor.execute(
            f"""
            CREATE TABLE {PRODUCTION_TABLE} AS
            SELECT * FROM {STAGING_TABLE}
            """
        )

    conn.commit()

    print(f"Registros promovidos: {total_records}")
    print("Promocao concluida com sucesso!")

except Exception as error:
    conn.rollback()
    print(f"Erro durante a promocao: {error}")
    print("Transacao desfeita. Dados anteriores preservados.")
    raise

finally:
    conn.close()

print("=" * 55)
