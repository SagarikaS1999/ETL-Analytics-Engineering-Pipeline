# 📦 ETL/ELT Analytics Engineering Pipeline
End-to-End Retail Analytics Platform using the Medallion Architecture (Bronze → Silver → Gold), DuckDB, PySpark, Airflow, and Power BI

## ⭐ 1. Overview
This project showcases a full analytics engineering workflow, designed as a take-home challenge to demonstrate:

- Data modeling
- Automation
- Pipeline engineering
- SQL Development
- KPI design
- Dashboard development
- PySpark analytics
- Airflow DAG orchestration

The goal is to simulate a real-world retail analytics pipeline that ingests ERP + CRM sales data, cleans it, models it using Medallion principles, generates KPIs, and feeds a Power BI dashboard.
This project is intentionally built for scalability, clarity, and enterprise-readiness.

## ⭐ 2. Data Architecture
<img width="893" height="625" alt="Data Architecture" src="https://github.com/user-attachments/assets/073b01e2-881e-4851-936a-e862ff888142" />

## ⭐ 3. Key Features
### ✔ Medallion Architecture (Bronze → Silver → Gold)
- Bronze: Raw ingestion with DuckDB
- Silver: Cleaned + conformed models
- Gold: Fact & Dim tables with surrogate keys

### ✔ PySpark Analytics Module
- Customer segmentation (High / Medium / Low) based on spending percentiles.

### ✔ Airflow DAG Overview
Tasks:
- ingest_bronze
- validate_data
- run_silver
- run_gold
- run_kpi
- run_pyspark_segmentation
- export_for_powerbi
DAG reflects a real Medallion workflow.

### ✔ Power BI Dashboard
- Executive Sales Overview
- Customer Insights
- Product & Category Performance

## ⭐ 4. Tech Stack
| Layer            | Tools / Technologies                         |
|------------------|-----------------------------------------------|
| Storage          | DuckDB                                        |
| Transformation   | SQL (Bronze, Silver, Gold)        |
| Processing       | PySpark                                       |
| Orchestration    | Apache Airflow                                |
| Visualization    | Power BI                                      |
| Programming      | Python, SQL, PySpark                                         |
| Data Modeling    | Medallion Architecture + Star Schema (SKs)    |

## ⭐ 5. Folder Structure
```
├── airflow_dags/
│   └── retail_pipeline_dag.py
├── pipeline/
│   ├── ingestion.py
│   ├── validation.py
│   ├── run_silver.py
│   ├── run_gold.py
│   └── run_kpi.py
├── spark/
│   └── customer_segmentation.py
├── models/
│   ├── silver/
│   ├── gold/
│   └── kpi/
├── exports/
│   ├── fact_sales.csv
│   ├── dim_customer.csv
│   └── dim_product.csv
└── README.md
```

## ⭐ 6. PySpark Module
File: spark/customer_segmentation.py
Implements:
- Load fact + dim datasets
- Join and aggregate customer revenue
- Compute percentiles
- Classify customers into:
  - High Value
  - Medium Value
  - Low Value
- Export for BI / ML use

## ⭐ 7. Airflow DAG
File: airflow_dags/retail_pipeline_dag.py
Pipeline tasks:
- Bronze ingestion
- Data validation
- Build Silver models
- Build Gold models
- Run PySpark segmentation
- Export CSVs for Power BI

## ⭐ 7. Business Insights (Sample Findings)
- Product Line R accounts for ~40% of total revenue
- Subcategory Helmets has the highest unit volume
- Customer segment “High Value” contributes over 55% of revenue
- Australia is the strongest region by total sales
- Revenue spikes during Nov–Jan (holiday period)
- Repeat customers generate 2.4× more revenue than one-time buyers

## ⭐ 8. Conclusion
This project demonstrates real-world analytics engineering skills:
- Data ingestion
- Data modeling
- Orchestration
- KPI engineering
- Distributed processing
- BI reporting
- Medallion architecture
