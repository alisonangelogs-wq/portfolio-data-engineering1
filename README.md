Pipeline de Dados de Controle de Jornada de Funcionários

Pipeline completo de Engenharia de Dados (end-to-end) desenvolvido para coletar, processar, armazenar e orquestrar dados de controle de ponto de funcionários.

Este projeto simula um fluxo de dados semelhante a um ambiente de produção, utilizando Docker, Apache Airflow, Python e SQL.

Objetivo do Projeto

Construir uma pipeline de dados capaz de:
Coletar registros de jornada de trabalho
Processar e validar dados brutos
Carregar dados tratados em um banco SQL
Automatizar todo o fluxo com Apache Airflow
Demonstrar habilidades reais de Engenharia de Dados em um projeto de portfólio
Este projeto reproduz um cenário real de ETL (Extract, Transform, Load).

Arquitetura da Pipeline

Fluxo de dados:

Fonte de dados (CSV / Gerador simulado)
        ↓
Scripts Python de ingestão
        ↓
Transformação e validação dos dados
        ↓
Banco de dados SQLite
        ↓
Orquestração com Apache Airflow (DAG)

Tecnologias Utilizadas

Tecnologia
Finalidade
Python
Scripts ETL
Apache Airflow
Orquestração de workflows
Docker
Ambiente containerizado
SQLite
Banco de dados relacional
Pandas
Transformação de dados
Git & GitHub
Versionamento de código

Estrutura do Projeto

employee_pipeline/
│
├── dags/
│   └── employee_pipeline_dag.py
│
├── data/
│   └── employee_times.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md

Modelo de Dados

Cada registro contém as seguintes colunas:
Coluna
Descrição
employee_id
Identificador do funcionário
check_in
Horário de entrada
lunch_out
Saída para almoço
lunch_in
Retorno do almoço
check_out
Horário de saída
work_hours
Horas trabalhadas (calculadas)

Pipeline ETL

-Extração (Extract)
Simula a geração de dados de controle de ponto por meio de arquivo CSV ou script Python.
-Transformação (Transform)
Processamentos realizados:
Conversão e padronização de datas e horários
Validação da qualidade dos dados
Cálculo automático das horas trabalhadas
Tratamento de registros inconsistentes ou incompletos
-Carga (Load)
Carregamento dos dados tratados no banco de dados SQLite.

Orquestração com Apache Airflow

A DAG executa automaticamente as etapas:
Extração
Transformação
Carga
A execução ocorre diariamente, simulando um ambiente de produção.

Como Executar o Projeto com Docker

1-Clonar o repositório
Bash
git clone https://github.com/your-user/portfolio-data-engineering1.git
cd portfolio-data-engineering

2-Subir os containers
Bash
docker-compose up -d

3-Acessar a interface do Airflow
Abra no navegador:

http://localhost:8080
Credenciais padrão:
Usuário: airflow
Senha: airflow

4-Executar a DAG
Abra a interface do Airflow
Localize a DAG employee_pipeline
Ative a DAG
Clique em Trigger DAG

Melhorias Futuras

Substituir SQLite por PostgreSQL
Criar camada de Data Warehouse
Adicionar testes automatizados
Fazer deploy em nuvem (AWS / GCP / Azure)
Criar dashboards (Power BI / Metabase)
Implementar ingestão via API

Habilidades Demonstradas

Desenvolvimento de pipelines ETL end-to-end
Orquestração de workflows com Airflow
Containerização com Docker
Modelagem e validação de dados
Automação de pipelines de dados

Autor

Alison Angelo Gomes da Silva
Professor de Física e Biologia em transição para Engenharia de Dados

Propósito

Projeto desenvolvido como parte de um portfólio profissional de Engenharia de Dados.