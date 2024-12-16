from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_hello_airflow():
    print("Hello Airflow")

with DAG(
        'hello_airflow_demo',
        schedule_interval=None,
        start_date=datetime(2024, 12, 3),
        catchup=False,
) as dag:


    hello_task = PythonOperator(
        task_id='print_hello_airflow_task',
        python_callable=print_hello_airflow,
    )


    hello_task
