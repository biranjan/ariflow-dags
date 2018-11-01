from airflow.operators.postgres_operator import PostgresOperator
import datetime as dt
from airflow import DAG

default_args = {
    'owner':'airflow',
    'start_date': dt.datetime.now(),
    'concurreny': 1,
    'retries':0
}

dag = DAG(
    'postgres_dag', default_args=default_args,\
     schedule_interval= '*/15 * * * *')



sql = """
CREATE TABLE IF NOT EXISTS test_airflow (
    dummy VARCHAR(50)
);
"""


p_task = PostgresOperator(
    postgres_conn_id='my_test_db',
    task_id='basic_mysql',
    sql=sql,
    dag=dag)
