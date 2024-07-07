from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

# DAG steps
def test():
    print("Started at " + str(datetime.now()))
    time.sleep(10)
    print("Done at " + str(datetime.now()))

# DAG defintion
dag = DAG('test_dag', schedule=None)
task = PythonOperator(task_id='test_task', python_callable=test, dag=dag)