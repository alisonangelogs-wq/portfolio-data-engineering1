# Employee Time Tracking Data Pipeline

This project simulates a simple end-to-end data pipeline for employee time tracking. It processes attendance records (entry, lunch break, return, and exit times) and stores the cleaned data in a structured database for analysis.

The main goal of this project is to practice core data engineering concepts using Airflow, Docker, Python, and SQL in a realistic workflow.

---

## Project overview

The pipeline handles the full data flow, from raw input to structured output:

- Ingests raw time tracking data  
- Cleans and standardizes timestamps  
- Calculates working hours and break durations  
- Performs basic data validation  
- Loads the final dataset into a SQL database  

All steps are orchestrated using Apache Airflow.

---

## Architecture

The pipeline follows a basic ETL flow:

Raw Data → Extract → Transform → Validate → Load → Database  

Airflow is responsible for scheduling and orchestration, while Docker is used to keep the environment consistent and reproducible.

---

## Tech stack

- Python (data processing and ETL logic)  
- Apache Airflow (workflow orchestration)  
- Docker / Docker Compose (environment setup)  
- SQL (SQLite / PostgreSQL)  
- Pandas (data manipulation)  

---

## Project structure

portfolio-data-engineering/

├── dags/                 # Airflow DAGs  
├── data/                 # Raw and processed data  
├── scripts/             # ETL scripts  
├── database/            # Schema or database files  
├── logs/                # Airflow logs  
├── docker-compose.yml   # Docker setup  
├── Dockerfile           # Airflow image build  
└── README.md  

---

## How to run

### 1. Clone the repository

git clone https://github.com/alisonangelogs-wq/portfolio-data-engineering1.git  
cd portfolio-data-engineering1  

---

### 2. Start the environment

docker compose up -d  

---

### 3. Access Airflow

Open in your browser:

http://localhost:8080  

Default credentials:
- username: airflow  
- password: airflow  

---

### 4. Run the pipeline

Trigger the DAG from the Airflow interface.

---

## What this project demonstrates

This project was built mainly to practice and reinforce:

- Basic ETL pipeline design  
- Airflow orchestration  
- Dockerized environments  
- Data cleaning and transformation logic  
- Thinking in terms of data flow instead of isolated scripts  

---

## Possible improvements

Some next steps that could evolve this project:

- Switch from SQLite to PostgreSQL  
- Add data quality checks (e.g. Great Expectations)  
- Include automated tests for transformations  
- Improve logging and error handling  
- Deploy to a cloud environment (AWS or GCP)  

---

## Author

Alison Angelo Gomes da Silva  
Data Engineer | Systems Analyst