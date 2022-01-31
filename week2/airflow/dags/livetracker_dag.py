import os
from datetime import date, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from extract import load_task
from transform import transform_task

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
STORAGE_DIR = "/livetracker"


default_args = {
    "owner": "airflow",
    "start_date": datetime.now(),
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="livetracker_dag",
    schedule_interval="*/5 * * * *",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
) as dag:

    load_json_task = PythonOperator(
        task_id='load_games_task',
        python_callable=load_task,
        op_kwargs={
            "path": AIRFLOW_HOME+STORAGE_DIR
        }
    )
    
    transform_json_task = PythonOperator(
        task_id='tranform_json_task',
        python_callable=transform_task,
        op_kwargs={
            "path": AIRFLOW_HOME+STORAGE_DIR,
            "timestamp": '{{ ti.xcom_pull(key=\'return_value\', task_ids=\'load_games_task\') }}'
            }
    )

    load_json_task >> transform_json_task