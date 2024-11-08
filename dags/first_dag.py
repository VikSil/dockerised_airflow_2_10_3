import airflow

from airflow import DAG
# VSCode will complain about the airflow sub-modules - you can ignore it
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator


from datetime import timedelta

import sys
sys.path.append('/opt/airflow/scripts')
# VSCode will complain about the module names - you can ignore it
from hello_world import greeting


DEFAULT_ARGS = {
    'depends_on_past': False,
    'owner': 'the_spinning_squirrel',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'start_date': airflow.utils.dates.days_ago(0),
}

dag = DAG(
    'first_dag',
    default_args=DEFAULT_ARGS,
    description='first attempt at a dag',
    schedule_interval=timedelta(minutes=5),
)

with dag:
    init_task = PythonOperator(
        task_id='init_task',
        python_callable=greeting,
        dag=dag,
    )

    init_task

