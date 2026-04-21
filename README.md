# Employee Time Tracking Data Pipeline

## Overview

This project is a professional Data Engineering pipeline designed to simulate an employee time tracking system in a production-like environment. It demonstrates an end-to-end data workflow including extraction, transformation, validation, orchestration, and loading into a relational database.

The solution uses Apache Airflow for workflow orchestration, Docker for environment standardization, Python for data processing, and SQL for data storage and querying.

## Business Objective

The objective of this pipeline is to process employee attendance data and transform it into structured and reliable information that can be used for workforce analysis, including working hours, attendance tracking, and productivity insights.

## Architecture

Data Source (CSV / Simulated Input)  
→ Apache Airflow DAG (Orchestration)  
→ Python ETL Layer (Processing & Transformation)  
→ Data Validation Layer (Data Quality Checks)  
→ SQL Database (SQLite / PostgreSQL)  
→ Analytics / Reporting Layer  

## Tech Stack

- Apache Airflow
- Docker & Docker Compose
- Python (Pandas, SQLAlchemy)
- SQL (SQLite / PostgreSQL)
- Git & GitHub

## Project Structure

dags/                  Airflow DAG definitions  
scripts/               ETL pipeline logic  
data/                  Input datasets  
logs/                  Execution logs  
docker-compose.yml     Airflow environment setup  
Dockerfile             Container configuration  
requirements.txt       Python dependencies  
README.md              Project documentation  

## Pipeline Workflow

### Extract
Raw employee attendance data is collected from structured input sources such as CSV files or simulated datasets.

### Transform
Data is cleaned and standardized, including:
- Date and time formatting
- Calculation of working hours
- Handling missing or inconsistent values

### Validate
Data quality checks are applied:
- Detection of missing values
- Identification of duplicate records
- Consistency validation rules

### Load
Processed data is stored in a relational database for querying and analysis.

## How to Run the Project

### Clone the repository
git clone https://github.com/alisonangelogs-wq/portfolio-data-engineering1.git  
cd portfolio-data-engineering1  

### Start the environment
docker-compose up -d  

### Access Airflow UI
http://localhost:8080  

## Example Output

Input data:

Employee | Check-in | Check-out | Date  
John     | 08:00    | 17:00      | 2026-04-01  

Output data:

- Total working hours per employee  
- Daily attendance metrics  
- Productivity indicators  

## Key Features

- End-to-end ETL pipeline  
- Modular Python architecture  
- Airflow orchestration  
- Containerized environment with Docker  
- Data validation layer  
- Reproducible setup  

## Future Improvements

- Migration to PostgreSQL for production use  
- Integration with Great Expectations for data quality  
- Unit and integration testing for ETL scripts  
- Dashboard integration (Power BI or Metabase)  
- CI/CD pipeline using GitHub Actions  
- Logging and monitoring improvements  

## Author

Alison Angelo Gomes da Silva  
Data Engineer | Python | Airflow | SQL | Docker  

## License

This project is for educational and professional portfolio purposes.