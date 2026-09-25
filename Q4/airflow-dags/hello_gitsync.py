from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello():
    print("Hello from GitSync")
    print("name=박주형")
    print("GitHub DAG sync success")


with DAG(
    dag_id="hello_gitsync",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["q4", "gitsync"],
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=hello,
    )