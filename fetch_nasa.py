import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from downl_img_to_fold_def import download_image_to_folder
from get_extension_def import get_extension
from dotenv import load_dotenv


def fetch_nasa_apod_image(payload):
    '''Функция получает фотографии NASA из раздела =APOD='''
    url_apod = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url_apod, params=payload)
    response.raise_for_status()
    response_json = response.json()
    if isinstance(response_json, dict):
        serial_number = datetime.now().date()
        path = f'images/apod/{serial_number}.{get_extension(response.json()["url"])}'
        download_image_to_folder(response.json()['url'], path, payload)
    else:
        for serial_number, response in enumerate(response_json):
            path = f'images/apod/{serial_number}.{get_extension(response["url"])}'
            download_image_to_folder(response['url'], path, payload)
        
        
def fetch_nasa_epic_image(payload):
    '''Функция получает фотографии NASA из раздела =EPIC='''
    url_epic = f'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url_epic, payload)
    response.raise_for_status()
    list_of_epic = []
    for item_response in response.json():
        name = item_response.get('image')
        date_time = datetime.fromisoformat(item_response.get('date'))
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        day = date_time.strftime("%d")
        epic_url = 'https://api.nasa.gov/EPIC/archive/natural'
        list_of_epic.append(
            f'{epic_url}/{year}/{month}/{day}/png/{name}.png'
        )
    for serial_number, item_url in enumerate(list_of_epic):
        path = f'images/epic/{serial_number}.{get_extension(item_url)}'
        download_image_to_folder(item_url, path, payload)


def main():
    load_dotenv()
    API_KEY_NASA = os.getenv('API_KEY_NASA')
    payload_apod = {
        'start_date': '', 
        'end_date': '',
        'api_key': API_KEY_NASA
    }
    payload = {'api_key': API_KEY_NASA}
    fetch_nasa_apod_image(payload_apod)
    #fetch_nasa_epic_image(payload)


if __name__ == '__main__':
    main()
