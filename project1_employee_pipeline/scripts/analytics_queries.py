import sqlite3

DB_PATH = "database/company.db"

def mostrar_resultado(titulo, cursor, formatar_horario=False):
    print(f"\n{titulo}")
    print("-" * 55)

    for row in cursor.fetchall():
        if formatar_horario:
            employee_id, segundos = row
            horas = int(segundos) // 3600
            minutos = (int(segundos) % 3600) // 60
            print(f"Funcionário {employee_id}: {horas:02d}:{minutos:02d}")
        else:
            print(row)


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    print("=" * 55)
    print("ANALISES DE JORNADA DOS FUNCIONARIOS")
    print("=" * 55)

    # 1. Atrasos
    cursor.execute("""
        SELECT employee_id, COUNT(*) AS late_days
        FROM employee_times
        WHERE check_in > '08:15:00'
        GROUP BY employee_id
        ORDER BY late_days DESC, employee_id
    """)
    mostrar_resultado("1. FUNCIONARIOS COM MAIS ATRASOS", cursor)

    # 2. Média do horário de saída
    cursor.execute("""
        SELECT employee_id,
               AVG(
                   CAST(strftime('%H', check_out) AS INTEGER) * 3600
                   + CAST(strftime('%M', check_out) AS INTEGER) * 60
                   + CAST(strftime('%S', check_out) AS INTEGER)
               )
        FROM employee_times
        GROUP BY employee_id
        ORDER BY employee_id
    """)
    mostrar_resultado("2. MEDIA DO HORARIO DE SAIDA", cursor, True)

    # 3. Dias trabalhados
    cursor.execute("""
        SELECT employee_id, COUNT(*) AS worked_days
        FROM employee_times
        GROUP BY employee_id
        ORDER BY employee_id
    """)
    mostrar_resultado("3. DIAS TRABALHADOS", cursor)

    # 4. Média de horas trabalhadas
    cursor.execute("""
        SELECT employee_id,
               AVG(
                   (strftime('%s', '1970-01-01 ' || lunch_out)
                    - strftime('%s', '1970-01-01 ' || check_in))
                   +
                   (strftime('%s', '1970-01-01 ' || check_out)
                    - strftime('%s', '1970-01-01 ' || lunch_in))
               )
        FROM employee_times
        GROUP BY employee_id
        ORDER BY employee_id
    """)
    mostrar_resultado("4. MEDIA DE HORAS TRABALHADAS", cursor, True)

    print("\nANALISES CONCLUIDAS")

finally:
    conn.close()
