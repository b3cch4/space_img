import os
import requests
from datetime import datetime
from download_image import download_image_to_folder
from get_extension_def import get_extension
from dotenv import load_dotenv


def fetch_nasa_apod_image(response_json, payload):
    '''Функция получает одну фотографию NASA из раздела =APOD='''
    serial_number = datetime.now().date()
    extension = get_extension(response_json["url"])
    path = f'images/apod/{serial_number}.{extension}'
    download_image_to_folder(response_json['url'], path, payload)


def fetch_nasa_epic_image(payload):
    '''Функция получает фотографии NASA из раздела =EPIC='''
    url_epic = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url_epic, payload)
    response.raise_for_status()
    urls_of_epic = []
    for item_response in response.json():
        name = item_response.get('image')
        date_time = datetime.fromisoformat(item_response.get('date'))
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        day = date_time.strftime("%d")
        epic_url = 'https://api.nasa.gov/EPIC/archive/natural'
        urls_of_epic.append(
            f'{epic_url}/{year}/{month}/{day}/png/{name}.png'
        )
    for serial_number, item_url in enumerate(urls_of_epic):
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
    url_apod = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url_apod, params=payload_apod)
    response.raise_for_status()
    response_from_apod = response.json()
    if isinstance(response_from_apod, dict):
        fetch_nasa_apod_image(response_from_apod, payload_apod)
    else:
        for serial_number, response in enumerate(response_from_apod):
            extension = get_extension(response["url"])
            path = f'images/apod/{serial_number}.{extension}'
            download_image_to_folder(response['url'], path, payload)
    fetch_nasa_epic_image(payload)


if __name__ == '__main__':
    main()
