import requests
import os
import mlflow

def download_data(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

# URL del file CSV da scaricare
csv_url = 'https://deliziedelparnaso.it/data.csv'
# Destinazione locale per il salvataggio del file CSV
csv_destination = 'data.csv'

# Esegui il download del file CSV
download_data(csv_url, csv_destination)

# Registra il file CSV scaricato come artefatto MLflow
with mlflow.start_run():
    mlflow.log_artifact(csv_destination, artifact_path='data')
