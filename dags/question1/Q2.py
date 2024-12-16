from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


def print_airflow_variable():

    my_var = Variable.get("my_variable")
    print(f"The value of the Airflow variable 'my_variable' is: {my_var}")


with DAG(
        'read_airflow_variable_demo',
        schedule_interval=None,
        start_date=datetime(2024, 12, 3),
        catchup=False,
) as dag:


    read_var_task = PythonOperator(
        task_id='print_airflow_variable_task',
        python_callable=print_airflow_variable,
    )


    read_var_task
