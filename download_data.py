import requests
import mlflow

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def main(file_url_p, destination_path_p):
    # Specifica l'URL del file remoto da scaricare
    #file_url = 'https://www.deliziedelparnaso.it/data.csv'
    file_url = file_url_p

    # Specifica il percorso di destinazione in cui salvare il file scaricato
    #destination_path = '/app/chris_python_download.csv'
    destination_path = destination_path_p 

    # Esegui il download del file remoto
    download_file(file_url, destination_path)

if __name__ == '__main__':
    with mlflow.start_run():
        file_url = mlflow.current_run().data.params.get("file_url_p")
        destination_path = mlflow.current_run().data.params.get("destination_path_p")
        main(file_url, destination_path)
