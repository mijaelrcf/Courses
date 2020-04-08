# Dentro de la carpeta de tu proyecto ejecutas
# virtualenv venv
# Activa el entorno virtual con el comando (en windows CMD)
# venv\Scripts\activate.bat
# para desactivar y salir del entorno virtual 
# deactivate

import requests
from bs4 import BeautifulSoup
import urllib.request

def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser') 
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        
        print('Descargando la imagen {}...'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == "__main__":
    run()
