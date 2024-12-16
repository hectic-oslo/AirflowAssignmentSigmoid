import json
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAAAj3kq2_c/messages?key=[placeholder]&token=[placeholder]"

def send_to_google_chat():

    message = Variable.get("google_chat_alert_message", default_var="No message set")


    payload = {
        "text": message
    }

    # Send the POST request to Google Chat
    response = requests.post(WEBHOOK_URL, json=payload)


    if response.status_code == 200:
        print("Message successfully sent to Google Chat!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")


with DAG(
        'google_chat_alert_dag',
        default_args={
            'owner': 'airflow',
            'retries': 1,
        },
        description='A simple DAG to send a message to Google Chat',
        schedule_interval=None,
        start_date=datetime(2024, 12, 15),
        catchup=False,
) as dag:


    send_alert_task = PythonOperator(
        task_id='send_alert_to_google_chat',
        python_callable=send_to_google_chat,
    )
