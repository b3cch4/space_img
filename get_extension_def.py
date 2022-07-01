import os
from urllib.parse import urlparse, unquote


def get_extension(url):
    '''Функция, возвращающая расширение файла'''
    full_url = unquote(url)
    path_of_url = urlparse(full_url).path
    full_name_of_picture = os.path.split(path_of_url)[-1]
    full_extension = os.path.splitext(full_name_of_picture)[-1]
    extension = full_extension[1:]
    return extension
