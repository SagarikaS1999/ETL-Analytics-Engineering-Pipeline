from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "sagar",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="retail_analytics_pipeline",
    default_args=default_args,
    description="Medallion-based Retail Analytics Pipeline using DuckDB + PySpark",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    # 1. Bronze Layer
    ingest_bronze = BashOperator(
        task_id="ingest_bronze",
        bash_command="python /opt/airflow/pipeline/data_ingestion.py"
    )

    # 2. Data Validation
    validate_data = BashOperator(
        task_id="validate_data",
        bash_command="python /opt/airflow/pipeline/validation.py"
    )

    # 3. Silver Layer
    run_silver = BashOperator(
        task_id="run_silver",
        bash_command="python /opt/airflow/pipeline/run_silver.py"
    )

    # 4. Gold Layer
    run_gold = BashOperator(
        task_id="run_gold",
        bash_command="python /opt/airflow/pipeline/run_gold.py"
    )

    # . PySpark customer segmentation
    run_pyspark_segmentation = BashOperator(
        task_id="run_pyspark_segmentation",
        bash_command="python /opt/airflow/spark/customer_segmentation.py"
    )

    # 6. Export CSVs for Power BI
    export_for_powerbi = BashOperator(
        task_id="export_for_powerbi",
        bash_command="duckdb /opt/airflow/warehouse.db \"EXPORT DATABASE 'exports' (FORMAT CSV, HEADER);\""
    )

    # DAG flow
    ingest_bronze >> validate_data >> run_silver >> run_gold >> run_pyspark_segmentation >> export_for_powerbi


#     This is the orchestrator layer of my project.
# I built a production-style Airflow DAG that automates ingestion, cleaning, modeling, and analytics.
# Each medallion layer is a separate task, so it’s easy to track failures, rerun specific layers, and scale the pipeline.
# I also included a PySpark job to demonstrate distributed analytics.
# Finally, the DAG exports a fresh set of CSVs for Power BI, making the dashboard automatically refreshable.