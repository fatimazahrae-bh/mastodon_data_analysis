from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import subprocess
import sys

default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 10, 23),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('Mastodon_Workflow', default_args=default_args, schedule_interval=None)

def set_data_path(**kwargs):
    data_path = get_data()  # Remplacez cette fonction par votre méthode de récupération de données Mastodon
    processed_path = '/processed/' + datetime.now().strftime('%Y-%m-%d/%H-%M') + '/'
    Variable.set("data_path", data_path)
    Variable.set("processed_path", processed_path)

retrieve_and_save_mastodon_data_task = PythonOperator(
    task_id='id_mastodon_data',
    provide_context=True,
    python_callable=set_data_path,
    dag=dag,
)

def run_map_reduce(**kwargs):
    data_path = Variable.get("data_path")
    output_path = Variable.get("processed_path")
    
    # Utilisez subprocess pour exécuter le travail Hadoop MapReduce
    hadoop_command = f"hadoop jar /usr/local/mastadon/hadoop-streaming-3.3.6.jar  " \
                     f"-mapper /home/bureau/Mastadon_data_analysis/mapReduce/mapper.py " \
                     f"-reducer /home/bureau/Mastadon_data_analysis/mapReduce/reducer.py " \                 
                     f"-input {data_path} " \
                     f"-output {output_path}"
    subprocess.run(hadoop_command, shell=True)

run_map_reduce_task = PythonOperator(
    task_id='run_map_reduce',
    provide_context=True,
    python_callable=run_map_reduce,
    dag=dag,
)

def run_hbase_insertion(**kwargs):
    processed_path = Variable.get("processed_path")
    insert_data_into_hbase(processed_path)  # Remplacez cette fonction par votre méthode d'insertion dans HBase

run_hbase_insertion_task = PythonOperator(
    task_id='run_hbase_insertion',
    provide_context=True,
    python_callable=run_hbase_insertion,
    dag=dag,
)

retrieve_and_save_mastodon_data_task >> run_map_reduce_task >> run_hbase_insertion_task

if __name__ == "__main__":
    dag.cli()
