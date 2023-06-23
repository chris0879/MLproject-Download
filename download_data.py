import requests
import os
import mlflow

def download_data(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        return True
    return False

# URL del file CSV da scaricare
csv_url = 'https://deliziedelparnaso.it/data.csv'
# Destinazione locale per il salvataggio del file CSV
csv_destination = 'data.csv'

# Esegui il download del file CSV
if download_data(csv_url, csv_destination):
    print("Il file è stato scaricato correttamente.")
else:
    print("Errore durante il download del file.")

# Registra il file CSV scaricato come artefatto MLflow
with mlflow.start_run():
    mlflow.log_artifact(csv_destination, artifact_path='data')
