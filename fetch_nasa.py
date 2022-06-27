import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from downl_img_to_fold_def import download_images_to_folder
from get_extension_def import get_extension
from dotenv import load_dotenv

load_dotenv()
API_KEY_NASA = os.getenv('API_KEY_NASA')

payload = {
    #'start_date': '2022-01-01', 
    #'end_date': '2022-01-04',
    'api_key': API_KEY_NASA
}
api_key = f'{API_KEY_NASA}'
url_apod = 'https://api.nasa.gov/planetary/apod'
url_epic = f'https://api.nasa.gov/EPIC/api/natural?api_key={API_KEY_NASA}'


def fetch_nasa_apod_images(url_apod, payload):
    '''Функция получает фотографии NASA из раздела =APOD='''
    response = requests.get(url_apod, params=payload)
    response.raise_for_status()
    if isinstance(response.json(), dict):
        serial_number = datetime.now().date()
        path = f'images/apod/{serial_number}.{get_extension(response.json()["url"])}'
        download_images_to_folder(response.json()['url'], path)
    else:
        for serial_number, response in enumerate(response.json()):
            path = f'images/apod/{serial_number}.{get_extension(response["url"])}'
            download_images_to_folder(response['url'], path)
        
        
def fetch_nasa_epic_images(url_epic, api_key):
    '''Функция получает фотографии NASA из раздела =EPIC='''
    response = requests.get(url_epic)
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
            f'{epic_url}/{year}/{month}/{day}/png/{name}.png?api_key={api_key}'
        )
    for serial_number, item_url in enumerate(list_of_epic):
        path = f'images/epic/{serial_number}.{get_extension(item_url)}' 
        download_images_to_folder(item_url, path)  


def main():
    fetch_nasa_apod_images(url_apod, payload)
    fetch_nasa_epic_images(url_epic, api_key)


if __name__ == '__main__':
    main()
