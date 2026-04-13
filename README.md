Employee Time Tracking Data Pipeline

End-to-end Data Engineering pipeline designed to collect, process, store and orchestrate employee time tracking data.

This project simulates a real production-like data workflow using Docker, Apache Airflow, Python and SQL.

Project Goal

Build a complete data pipeline capable of:

Collecting employee work time records
Processing and validating the data
Loading into a SQL database
Automating the workflow with Airflow
Demonstrating real Data Engineering skills for portfolio purposes

This project reproduces a real-world data engineering scenario.

Pipeline Architecture

Data flow:

Data source (CSV / simulated generator)
        ↓
Python ingestion scripts
        ↓
Data transformation & validation
        ↓
Load into SQLite database
        ↓
Airflow orchestration (DAG)

Tech Stack

Technology	Purpose
Python	ETL scripts
Apache Airflow	Workflow orchestration
Docker	Containerized environment
SQLite	Database
Pandas	Data transformation
Git & GitHub	Version control

Project Structure

employee_pipeline/

dags/ 
employee_pipeline_dag.py

data/ 
employee_times.csv

scripts/ 
extract.py
transform.py
load.py

docker-compose.yml
requirements.txt
README.md

Data Model

Each record contains:

Column	Description
employee_id	Employee ID
check_in	Work start time
lunch_out	Lunch break start
lunch_in	Lunch break end
check_out	Work end time
work_hours	Calculated worked hours
ETL Pipeline
Extract

Simulates employee time tracking data generation.

Transform

Data processing includes:

Datetime parsing
Data validation
Work hours calculation
Handling inconsistent records
Load

Loads the processed dataset into SQLite database.

Airflow Orchestration

The DAG automatically runs:

Data extraction
Data transformation
Data loading

Runs daily to simulate a production environment.

Running the Project with Docker
Clone the repository
git clone https://github.com/your-user/portfolio-data-engineering1.git
cd portfolio-data-engineering
Start the containers
docker-compose up -d
Access Airflow UI

Open in your browser:

http://localhost:8080

Default credentials:

user: airflow
password: airflow
Trigger the DAG
Open Airflow UI
Find: employee_pipeline
Enable the DAG
Click Trigger DAG
Future Improvements
Replace SQLite with PostgreSQL
Build a Data Warehouse layer
Add automated tests
Deploy to cloud (AWS / GCP / Azure)
Create dashboards (Power BI / Metabase)
Add API ingestion
Skills Demonstrated

This project showcases:

Data Engineering fundamentals
ETL pipeline development
Docker & containerization
Airflow orchestration
Git version control
Data modeling
Workflow automation

Author

Alison Angelo Gomes da Silva
Physics & Biology Teacher transitioning into Data Engineering

Purpose

Project developed as part of a professional Data Engineering portfolio.
