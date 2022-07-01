import os, requests


def download_image_to_folder(url, path):
    '''Функция загружает фотографии по ссылке, полученной в качестве аргумента <url>'''
    os.makedirs(os.path.dirname(path), exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)