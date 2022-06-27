import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from downl_img_to_fold_def import download_images_to_folder
from get_extension_def import get_extension

url = 'https://api.spacexdata.com/v4/launches/'

def fetch_spacex_last_launch(url):
        '''Функция получает фотографии последнего запуска шатла.'''
        response = requests.get(url)
        response.raise_for_status()
        #print(type(not (response.json())[-1]['links']['flickr']['original']))
        for item in reversed(response.json()):
            if item['links']['flickr']['original']:
                list_of_spacex_links = item['links']['flickr']['original']
                break
        for serial_number, link in enumerate(list_of_spacex_links):
            path = f'images/spacex/{serial_number}.{get_extension(link)}'
            download_images_to_folder(link, path)

def main():
    fetch_spacex_last_launch(url)

if __name__ == '__main__':
    main()
