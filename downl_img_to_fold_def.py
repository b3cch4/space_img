import os, requests


def download_images_to_folder(url, path):
    '''Функция загружает фотографии по ссылке, полученной в качестве аргумента <url>'''
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)