# Data Engineering Portfolio – ETL Pipeline with Apache Airflow

## Overview

This project implements an end-to-end Data Engineering ETL pipeline orchestrated with Apache Airflow and containerized using Docker.

The pipeline automates the process of extracting data from a source, transforming and cleaning the data using Python, and loading the processed data into a target storage system.

The goal of this project is to simulate a real-world data engineering workflow, demonstrating skills in data orchestration, pipeline design, and containerized environments.

---

## Architecture

The pipeline follows the ETL (Extract, Transform, Load) pattern:

Data Source → Extract → Transform → Load → Output Storage

Orchestration is handled by Apache Airflow running inside Docker containers.

---

## Technologies Used

- Apache Airflow  
- Python (Pandas)  
- Docker & Docker Compose  
- PostgreSQL or SQLite  
- Git & GitHub  

---

## Project Structure

portfolio-data-engineering/
│
├── dags/                  Airflow DAG definitions  
├── scripts/               ETL logic (extract, transform, load)  
├── data/                  Input and output data files (if applicable)  
├── docker-compose.yml    Airflow environment setup  
├── requirements.txt      Python dependencies  
└── README.md             Project documentation  

---

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/alisonangelogs-wq/portfolio-data-engineering1.git  
cd portfolio-data-engineering1  

---

### 2. Start Docker environment

Make sure Docker Desktop is running, then execute:

docker compose up -d  

---

### 3. Access Apache Airflow

Open your browser:

http://localhost:8080  

Default credentials:

Username: airflow  
Password: airflow  

---

## Pipeline Workflow

Extract  
Data is collected from a source (CSV, API, or simulated dataset).

Transform  
Data is cleaned and processed using Python (Pandas), including handling missing values, formatting, and normalization.

Load  
The transformed data is stored in a database or file system.

All steps are orchestrated using Apache Airflow DAGs.

---

## Airflow DAG Structure

The pipeline is executed in sequential tasks:

- extract_task  
- transform_task  
- load_task  

Dependencies are managed by Airflow to ensure correct execution order.

---

## Key Features

- End-to-end ETL pipeline  
- Workflow orchestration with Apache Airflow  
- Containerized environment with Docker  
- Modular Python scripts  
- Scalable and production-style structure  

---

## How Recruiters Should Evaluate This Project

This project should be evaluated based on the following criteria:

- Understanding of ETL pipeline architecture  
- Ability to orchestrate workflows using Apache Airflow  
- Code modularization and maintainability  
- Use of Docker for environment consistency  
- Data processing with Python (Pandas)  
- Awareness of real-world data engineering practices  

---

## Future Improvements

- Integration with cloud storage (AWS S3 or GCP)  
- Use of real-time APIs as data source  
- Data quality validation layer  
- Monitoring and alerting system (email or Slack)  
- CI/CD pipeline for automated deployment  

---

## Author

Alison Angelo Gomes da Silva  
Data Engineer in development | Background in Systems Analysis and Development (ADS)

---

## Final Notes

This project demonstrates practical skills in data pipeline development, workflow orchestration with Apache Airflow, containerization using Docker, Python data processing, and modern data engineering practices.