# Employee Time Tracking Data Pipeline

## Overview

An end-to-end Data Engineering project that processes employee attendance records using Python, SQL, SQLite, Docker, and Apache Airflow.

The pipeline extracts attendance data from a CSV file, loads it into a relational database, validates data quality, and executes SQL analytics.

The project simulates a real-world business scenario and demonstrates practical data engineering concepts, including ETL, workflow orchestration, data validation, and analytical queries.

## Business Objective

The objective is to transform employee attendance records into structured information that supports workforce monitoring and operational analysis.

The pipeline provides insights into:

- Employee attendance and punctuality
- Average check-out times
- Number of recorded working days
- Average daily working hours, excluding lunch breaks

## Architecture

CSV Dataset → Apache Airflow → Python ETL → SQLite → Data Quality Validation → SQL Analytics

## Tech Stack

- Python - ETL processing and data validation
- SQL - Analytical queries
- SQLite - Relational database
- Apache Airflow 3.3.2 - Workflow orchestration
- Docker - Containerization
- Docker Compose - Environment management
- Git and GitHub - Version control

## Pipeline Workflow

The Apache Airflow DAG coordinates three sequential tasks.

### 1. ETL - Data Extraction and Loading

- Reads employee attendance records from CSV.
- Processes the dataset using Python.
- Loads the records into the SQLite database.

### 2. Data Quality Validation

- Checks missing mandatory fields.
- Detects duplicate records.
- Validates time values and chronological consistency.
- Checks working time consistency.

The pipeline stops if the validation task detects inconsistencies.

### 3. SQL Analytics

The analytics script executes four SQL queries:

1. Employees with the highest number of late arrivals (check-in after 08:15).
2. Average check-out time per employee.
3. Number of recorded working days per employee.
4. Average daily working hours, excluding lunch breaks.

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
4. Follow the execution of the three tasks.

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
│   └── scripts/
│       ├── analytics_queries.py
│       ├── data_quality.py
│       ├── employee_time_tracking_pipeline.py
│       ├── etl_to_sqlite.py
│       └── generate_fake_date.py
├── .gitignore
├── compose.airflow.yaml
├── Dockerfile.airflow
└── README.md
```

## Key Features

- End-to-end ETL workflow
- Sequential task orchestration with Apache Airflow
- Automated data quality validation
- SQL-based workforce analytics
- SQLite relational database
- Docker-based execution environment

## Future Improvements

- PostgreSQL integration
- Automated unit and integration testing
- Advanced data quality framework integration
- Data visualization with Power BI or Metabase
- CI/CD automation with GitHub Actions
- Improved logging and monitoring

## Author

**Alison Angelo**

Data Engineering in Progress | Python | SQL | SQLite | Apache Airflow | Docker

## Project Purpose

Educational and professional portfolio project developed to demonstrate practical Data Engineering skills.
