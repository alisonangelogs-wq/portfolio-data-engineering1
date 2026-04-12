import sqlite3
import pandas as pd

DB_PATH = "database/company.db"

conn = sqlite3.connect(DB_PATH)

print("\nFuncionários que mais atrasaram (check-in após 08:15):")

query_late = """
SELECT employee_id, COUNT(*) AS late_days
FROM employee_times
WHERE check_in > '08:15:00'
GROUP BY employee_id
ORDER BY late_days DESC
"""

df_late = pd.read_sql(query_late, conn)
print(df_late)


print("\nMédia de horário de saída:")

query_exit = """
SELECT employee_id, AVG(strftime('%H', check_out)) AS avg_exit_hour
FROM employee_times
GROUP BY employee_id
"""

df_exit = pd.read_sql(query_exit, conn)
print(df_exit)


print("\nQuantidade de dias trabalhados por funcionário:")

query_days = """
SELECT employee_id, COUNT(*) AS worked_days
FROM employee_times
GROUP BY employee_id
"""

df_days = pd.read_sql(query_days, conn)
print(df_days)

conn.close()