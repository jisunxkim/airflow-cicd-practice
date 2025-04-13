from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("👋 Hello from the DEV DAG!")

with DAG(
    dag_id='simple_dag__dev',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello
    )
# Add dependencies if needed