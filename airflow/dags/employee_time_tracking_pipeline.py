from pathlib import Path
import subprocess
import sys

import pendulum
from airflow.sdk import dag, task


PROJECT_DIR = Path("/opt/airflow/employee_pipeline")


@dag(
    dag_id="employee_time_tracking_pipeline",
    description="Pipeline ETL com staging, qualidade de dados e analises SQL",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["engenharia-de-dados", "etl", "python", "sqlite", "qualidade"],
)
def employee_time_tracking_pipeline():

    @task
    def executar_etl():
        script = PROJECT_DIR / "scripts" / "etl_to_sqlite.py"

        if not script.exists():
            raise FileNotFoundError(f"Script nao encontrado: {script}")

        subprocess.run(
            [sys.executable, str(script)],
            cwd=str(PROJECT_DIR),
            check=True,
        )

    @task
    def validar_qualidade():
        script = PROJECT_DIR / "scripts" / "data_quality.py"

        if not script.exists():
            raise FileNotFoundError(f"Script nao encontrado: {script}")

        subprocess.run(
            [sys.executable, str(script)],
            cwd=str(PROJECT_DIR),
            check=True,
        )

    @task
    def promover_dados():
        script = PROJECT_DIR / "scripts" / "promote_to_production.py"

        if not script.exists():
            raise FileNotFoundError(f"Script nao encontrado: {script}")

        subprocess.run(
            [sys.executable, str(script)],
            cwd=str(PROJECT_DIR),
            check=True,
        )

    @task
    def executar_analises():
        script = PROJECT_DIR / "scripts" / "analytics_queries.py"

        if not script.exists():
            raise FileNotFoundError(f"Script nao encontrado: {script}")

        subprocess.run(
            [sys.executable, str(script)],
            cwd=str(PROJECT_DIR),
            check=True,
        )

    etl = executar_etl()
    qualidade = validar_qualidade()
    promocao = promover_dados()
    analises = executar_analises()

    etl >> qualidade >> promocao >> analises


employee_time_tracking_pipeline()
