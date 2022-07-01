import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from downl_img_to_fold_def import download_image_to_folder
from get_extension_def import get_extension


def fetch_spacex_last_launch():
        '''Функция получает фотографии последнего запуска шатла.'''
        url = 'https://api.spacexdata.com/v4/launches/'
        response = requests.get(url)
        response.raise_for_status()
        for item in reversed(response.json()):
            if item['links']['flickr']['original']:
                list_of_spacex_links = item['links']['flickr']['original']
                break
        for serial_number, link in enumerate(list_of_spacex_links):
            path = f'images/spacex/{serial_number}.{get_extension(link)}'
            payload = {}
            download_image_to_folder(link, path, payload)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
