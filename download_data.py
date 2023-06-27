import requests

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def main():
    # Specifica l'URL del file remoto da scaricare
    file_url = 'https://www.deliziedelparnaso.it/data.csv'

    # Specifica il percorso di destinazione in cui salvare il file scaricato
    destination_path = '/example/chris_python_download2.csv'

    # Esegui il download del file remoto
    download_file(file_url, destination_path)

if __name__ == '__main__':
    main()
