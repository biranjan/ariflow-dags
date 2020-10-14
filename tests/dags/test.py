import datetime as dt

from airflow import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator

sshHook = SSHHook(ssh_conn_id='test_server')
default_args = {
    'owner':'airflow',
    'start_date': dt.datetime.now(),
    'concurreny': 1,
    'retries':0
}

dag = DAG(
    'bash_dag', default_args=default_args,\
     schedule_interval= '*/15 * * * *')

bash_task = SSHOperator( task_id='create_file',
    ssh_hook=sshHook,
    command='touch /home/biranjan/airflow.txt && \
     echo "try" >> airflow.txt',
    dag=dag)

