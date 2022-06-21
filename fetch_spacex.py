import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from get_extension_def import get_extension
from downl_img_to_fold_def import downl_img_to_fold


def fetch_spacex_last_launch(url_spacex, path_spacex):
    '''Функция получает фотографии последнего запуска шатла.'''
    response = requests.get(url_spacex)
    response.raise_for_status()
    for item in reversed(response.json()):
        if item['links']['flickr']['original'] != []:
            list_of_spacex_links = item['links']['flickr']['original']
            break
    for serial_number, link in enumerate(list_of_spacex_links):
        downl_img_to_fold(link, path_spacex, serial_number)
