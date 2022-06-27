import os
import time
import asyncio
import telegram
from dotenv import load_dotenv


API_BOT = os.getenv('API_BOT')
CHAT_ID = os.getenv('CHAT_ID')


async def main():
    load_dotenv()
    while True:
        bot = telegram.Bot(API_BOT)
        for address, dirs, files in os.walk('images'):
            time.sleep(10)
            for name in files:
                async with bot:
                    await bot.send_document(
                        chat_id=int(CHAT_ID),
                        #can't find solution for (15 of 16)
                        document=open(os.path.join(address, name), 'rb')
                    )


if __name__ == '__main__':
    asyncio.run(main())
