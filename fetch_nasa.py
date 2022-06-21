import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote
from downl_img_to_fold_def import download_images_to_folder
from dotenv import load_dotenv

load_dotenv()
API_KEY_NASA = os.getenv('API_KEY_NASA')

payload_apod = {
    #'start_date': '2022-01-01', 
    #'end_date': '2022-01-04',
    'api_key': API_KEY_NASA
}
api_key = f'{API_KEY_NASA}'
url_apod = 'https://api.nasa.gov/planetary/apod'
url_epic = f'https://api.nasa.gov/EPIC/api/natural?api_key={API_KEY_NASA}'
path_apod = "images/apod"
path_epic = "images/epic"

def fetch_nasa_apod_images(url_apod, payload, path_apod):
    '''Функция получает фотографии NASA из раздела =APOD='''
    response = requests.get(url_apod, params=payload)
    response.raise_for_status()
    if type(response.json()) == dict:
        serial_number = datetime.now().date()
        download_images_to_folder(response.json()['url'], path_apod, serial_number)
    else:
        for serial_number, response in enumerate(response.json()):
            download_images_to_folder(response['url'], path_apod, serial_number)
        
        
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
        download_images_to_folder(item_url, path_epic, serial_number)    


def main():
    fetch_nasa_apod_images(url_apod, payload_apod, path_apod)
    fetch_nasa_epic_images(url_epic, path_epic, api_key)


if __name__ == '__main__':
    main()
