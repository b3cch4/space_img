import os
import time
import asyncio
import telegram
from dotenv import load_dotenv


API_BOT = os.getenv('API_BOT')
CHAT_ID = os.getenv('CHAT_ID')


async def main():
    load_dotenv()
    bot = telegram.Bot(API_BOT)
    while True:
        for address, dirs, files in os.walk('images'):
            for name in files:
                async with bot:
                    with open(os.path.join(address, name), 'rb') as img:                    
                        await bot.send_document(
                            chat_id=int(CHAT_ID),
                            document = img
                        )
        time.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())
