import os
import requests


def download_image_to_folder(url, path, payload):
    '''Функция загружает фотографии по ссылке, 
        полученной в качестве аргумента <url>'''
    os.makedirs(os.path.dirname(path), exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
