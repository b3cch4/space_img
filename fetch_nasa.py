import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from get_extension_def import get_extension
from downl_img_to_fold_def import downl_img_to_fold


def fetch_nasa_apod_images(url_apod, payload, path_apod):
    '''Функция получает фотографии NASA из раздела =APOD='''
    response = requests.get(url_apod, params=payload)
    response.raise_for_status()
    if type(response.json()) == dict:
        serial_number = datetime.now().date()
        downl_img_to_fold(response.json()['url'], path_apod, serial_number)
    else:
        for serial_number, response in enumerate(response.json()):
            downl_img_to_fold(response['url'], path_apod, serial_number)
        
        
def fetch_nasa_epic_images(url_epic, path_epic, api_key):
    '''Функция получает фотографии NASA из раздела =EPIC='''
    response = requests.get(url_epic)
    response.raise_for_status()
    list_of_epic = []
    for item_responce in response.json():
        name = item_responce.get('image')
        date_time = datetime.fromisoformat(response.json()[0].get('date'))
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        day = date_time.strftime("%d")
        epic_url = 'https://api.nasa.gov/EPIC/archive/natural'
        list_of_epic.append(
            f'{epic_url}/{year}/{month}/{day}/png/{name}.png?api_key={api_key}'
        )
    for serial_number, item_url in enumerate(list_of_epic):
        downl_img_to_fold(item_url, path_epic, serial_number)    

