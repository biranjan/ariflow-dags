from datetime import datetime,timedelta
from airflow import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator

sshHook = SSHHook(ssh_conn_id='test_server')
default_args = {
    'owner':'airflow',
    'start_date': datetime.now(),
    'concurreny': 1,
    'retries':0
}

dag = DAG(
    'docker_dag', default_args=default_args,\
     schedule_interval= timedelta(minutes=5))

bash_task = SSHOperator( task_id='create_backup',
    ssh_hook=sshHook,
    command='docker exec -i a13b7acfdcfa su postgres bash -c "pg_dump postgres | gzip > /var/lib/postgresql/data/test_Backup1.gz"',
    dag=dag)

bash_task2 = SSHOperator( task_id='copy_backup',
    ssh_hook=sshHook,
    command='docker cp a13b7acfdcfa:/var/lib/postgresql/data/test_Backup1.gz /home/biranjan/',
    dag=dag)

bash_task2.set_upstream(bash_task)