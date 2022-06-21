import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from downl_img_to_fold_def import ddownload_images_to_folder

url_spacex = 'https://api.spacexdata.com/v4/launches/'
path_spacex = "images/spacex"

def fetch_spacex_last_launch(url_spacex, path_spacex):
        '''Функция получает фотографии последнего запуска шатла.'''
        response = requests.get(url_spacex)
        response.raise_for_status()
        for item in reversed(response.json()):
            if item['links']['flickr']['original'] != []:
                list_of_spacex_links = item['links']['flickr']['original']
                break
        for serial_number, link in enumerate(list_of_spacex_links):
            download_images_to_folder(link, path_spacex, serial_number)

def main():
    fetch_spacex_last_launch(url_spacex, path_spacex)

if __name__ == '__main__':
    main()
