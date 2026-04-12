import pandas as pd
import random
from datetime import datetime, timedelta

# quantidade de funcionários
NUM_EMPLOYEES = 10

# quantidade de dias simulados
NUM_DAYS = 30

def generate_time(base_time, variation_minutes=15):
    variation = random.randint(-variation_minutes, variation_minutes)
    return (base_time + timedelta(minutes=variation)).time()

data = []

start_date = datetime.today() - timedelta(days=NUM_DAYS)

for day in range(NUM_DAYS):
    current_date = start_date + timedelta(days=day)

    for emp_id in range(1, NUM_EMPLOYEES + 1):

        check_in_base = datetime.combine(current_date, datetime.strptime("08:00", "%H:%M").time())
        lunch_out_base = datetime.combine(current_date, datetime.strptime("12:00", "%H:%M").time())
        lunch_in_base = datetime.combine(current_date, datetime.strptime("13:00", "%H:%M").time())
        check_out_base = datetime.combine(current_date, datetime.strptime("17:00", "%H:%M").time())

        row = {
            "employee_id": emp_id,
            "date": current_date.date(),
            "check_in": generate_time(check_in_base),
            "lunch_out": generate_time(lunch_out_base),
            "lunch_in": generate_time(lunch_in_base),
            "check_out": generate_time(check_out_base),
        }

        data.append(row)

df = pd.DataFrame(data)

df.to_csv("data/employee_times.csv", index=False)

print("Arquivo gerado com sucesso!")