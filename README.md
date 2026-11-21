
# Employee Time Tracking Data Pipeline

## Overview

An end-to-end Data Engineering project that processes employee attendance records using Python, SQL, SQLite, Docker, and Apache Airflow.

The pipeline extracts attendance data from a CSV file, loads it into a staging table, validates data quality, promotes approved records to a production table, and executes SQL analytics.

The project simulates a real-world business scenario and demonstrates practical data engineering concepts, including ETL, workflow orchestration, data quality validation, transactional data promotion, and analytical queries.

## Business Objective

The objective is to transform employee attendance records into structured information that supports workforce monitoring and operational analysis.

The pipeline provides insights into:

- Employee attendance and punctuality
- Average check-out times
- Number of recorded working days
- Average daily working hours, excluding lunch breaks

## Architecture

CSV Dataset → Apache Airflow → Python ETL → SQLite Staging → Data Quality Validation → Transactional Promotion → Production Table → SQL Analytics

## Tech Stack

- Python - ETL processing and data validation
- SQL - Analytical queries
- SQLite - Relational database
- Apache Airflow 3.3.2 - Workflow orchestration
- Docker - Containerization
- Docker Compose - Environment management
- Git and GitHub - Version control

## Pipeline Workflow

The Apache Airflow DAG coordinates four sequential tasks.

### 1. ETL - Data Extraction and Loading

- Reads employee attendance records from CSV.
- Processes the dataset using Python and Pandas.
- Loads the records into the `employee_times_staging` table.
- Replaces the staging data on each execution.

### 2. Data Quality Validation

The validation script checks:

- Missing mandatory fields.
- Duplicate employee records by employee and date.
- Invalid time values.
- Chronological consistency of attendance records.
- Working time consistency.

The pipeline stops if inconsistencies are detected.

### 3. Transactional Data Promotion

After successful validation, the promotion script:

- Checks whether the staging table exists.
- Verifies that staging contains records.
- Updates the `employee_times` production table.
- Uses an SQLite transaction to protect the production data.
- Rolls back the transaction if promotion fails.

This approach prevents invalid or incomplete data from replacing the production dataset when validation fails or promotion encounters an error.

### 4. SQL Analytics

The analytics script executes four SQL queries:

1. Employees with the highest number of late arrivals (check-in after 08:15).
2. Average check-out time per employee.
3. Number of recorded working days per employee.
4. Average daily working hours, excluding lunch breaks.

## Data Validation and Testing

The pipeline was tested with both valid and invalid attendance records.

### Valid dataset

- 300 records processed.
- No missing mandatory fields.
- No duplicate records.
- No invalid time values.
- No chronological inconsistencies.
- No invalid working durations.

### Invalid dataset

A test record was modified with a check-out time earlier than the lunch departure time.

The quality validation detected the chronological inconsistency. The invalid data remained in staging, while the production table preserved the previously approved record.

This test demonstrated the separation between staging and production and the importance of data quality checks before promotion.

## How to Run the Project

### Prerequisites

- Git
- Docker
- Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/alisonangelogs-wq/portfolio-data-engineering1.git
cd portfolio-data-engineering1
```

### 2. Build and start Airflow

```bash
docker compose -f compose.airflow.yaml up -d --build
```

### 3. Access the Airflow interface

Open http://localhost:8080 in your browser.

The standalone Airflow environment generates initial login credentials. Check the container logs if necessary:

```bash
docker logs employee_time_tracking_airflow 2>&1 | grep -i -E "password|username"
```

### 4. Execute the pipeline

1. Locate `employee_time_tracking_pipeline` in the Airflow interface.
2. Enable the DAG if it is paused.
3. Trigger a manual execution.
4. Follow the four tasks:
   - `executar_etl`
   - `validar_qualidade`
   - `promover_dados`
   - `executar_analises`

### 5. Stop the environment

```bash
docker compose -f compose.airflow.yaml down
```

## Project Structure

```text
portfolio-data-engineering1/
├── airflow/
│   └── dags/
│       └── employee_time_tracking_pipeline.py
├── project1_employee_pipeline/
│   ├── data/
│   │   └── employee_times.csv
│   ├── database/
│   │   └── company.db
│   └── scripts/
│       ├── analytics_queries.py
│       ├── data_quality.py
│       ├── employee_time_tracking_pipeline.py
│       ├── etl_to_sqlite.py
│       ├── generate_fake_date.py
│       └── promote_to_production.py
├── .gitignore
├── compose.airflow.yaml
├── Dockerfile.airflow
└── README.md
```

## Key Features

- End-to-end ETL workflow.
- Apache Airflow orchestration with four sequential tasks.
- Separate staging and production tables.
- Automated data quality validation.
- Transactional data promotion using SQLite.
- SQL-based workforce analytics.
- Docker-based execution environment.

## Future Improvements

- PostgreSQL integration into the main pipeline.
- Automated unit and integration testing.
- Advanced data quality framework integration.
- Data visualization with Power BI or Metabase.
- CI/CD automation with GitHub Actions.
- Improved logging and monitoring.

## Author

**Alison Angelo**

Data Engineering in Progress | Python | SQL | SQLite | Apache Airflow | Docker

## Project Purpose

Educational and professional portfolio project developed to demonstrate practical Data Engineering skills.
