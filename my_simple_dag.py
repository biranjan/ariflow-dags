import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def greet():
    print('Writing in file')
    with open('/home/greet.txt', 'a+', encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'

def respond():
    return 'Greet Responded Again'
    
default_args = {
    'owner':'airflow',
    'start_date': dt.datetime.now(),
    'concurreny': 1,
    'retries':0
}

dag = DAG(
    'my_simple_dag', default_args=default_args, schedule_interval= '*/10 * * * *')

opr_hello = BashOperator(task_id = 'say_Hi',
                            bash_command='echo "Hi!!"',
                            dag=dag)

opr_greet = PythonOperator(task_id='greet',
                                python_callable=greet,
                                dag=dag)
    
opr_hello >> opr_greet