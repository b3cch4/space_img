import os
from urllib.parse import urlparse, unquote


def get_extension(url):
    '''Функция, возвращающая расширение файла'''
    full_url = unquote(url)
    path_of_url = urlparse(full_url).path
    name_of_image = os.path.split(path_of_url)[-1]
    extension_with_dot = os.path.splitext(name_of_image)[-1]
    extension = extension_with_dot[1:]
    return extension
