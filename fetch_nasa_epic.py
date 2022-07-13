import os
import requests
from datetime import datetime
from download_image import download_image_to_folder
from get_extension import get_extension
from dotenv import load_dotenv


def fetch_nasa_epic_image(payload):
    '''Функция получает фотографии NASA из раздела =EPIC='''
    url_epic = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url_epic, payload)
    response.raise_for_status()
    urls_of_epic = []
    for item_response in response.json():
        name = item_response['image']
        date_time = datetime.fromisoformat(item_response['date'])
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
    payload_epic = {'api_key': API_KEY_NASA}
    fetch_nasa_epic_image(payload_epic)


if __name__ == '__main__':
    main()
