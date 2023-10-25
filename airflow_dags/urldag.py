from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default_args for your DAG
default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 10, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create an instance of the DAG
dag = DAG(
    'Dagurl',
    default_args=default_args,
    description='Data pipeline for collecting and analyzing data from Mastodon',
    schedule_interval=timedelta(minutes=2),  # Updated to run every 2 minutes
    catchup=False,
)

# Define tasks in your DAG
# Task to run the Hadoop streaming job
run_hadoop_job = BashOperator(
    task_id='run_hadoop_job',
    bash_command="hadoop jar /home/hadoop/mastodon/hadoop-streaming-2.7.3.jar -input /Mostodon/Raw/mastodon_data_2023-10-23.json -output /Mostodon/Raw/urlExternOutput -mapper /home/hadoop/mastodon/mapperURLex.py -reducer /home/hadoop/mastodon/reducerURLex.py",
    dag=dag,
)

# Set task dependencies
run_hadoop_job

if __name__ == "__main__":
    dag.cli()

