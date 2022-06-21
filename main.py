import os
import time
import asyncio
import telegram
from fetch_nasa import fetch_nasa_apod_images, fetch_nasa_epic_images
from fetch_spacex import fetch_spacex_last_launch
from dotenv import load_dotenv

load_dotenv()

API_KEY_NASA = os.getenv('API_KEY_NASA')
API_BOT = os.getenv('API_BOT')
CHAT_ID = os.getenv('CHAT_ID')

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
url_spacex = 'https://api.spacexdata.com/v4/launches/'
path_spacex = "images/spacex"

async def main():
    while True:
        time.sleep(10)
        fetch_nasa_apod_images(url_apod, payload_apod, path_apod)
        fetch_nasa_epic_images(url_epic, path_epic, api_key)
        fetch_spacex_last_launch(url_spacex, path_spacex)
        bot = telegram.Bot(API_BOT)
        for address, dirs, files in os.walk('images'):
            for name in files:
                async with bot:
                    await bot.send_document(
                        chat_id=int(CHAT_ID),
                        document=open(os.path.join(address, name), 'rb')
                    )


if __name__ == '__main__':
    asyncio.run(main())
