
<h1 align="center">Скрипт для загрузки фотографий космоса</h1>

## Описание

Скрипты скачивают фотографи космоса с сайта [NASA](https://api.nasa.gov/) из разделов [APOD](https://api.nasa.gov/#apod) и [EPIC](https://api.nasa.gov/#epic), а также фотографии последнего запуска космических шатлов [SpaceX](https://github.com/r-spacex/SpaceX-API) загружают их локально в папку **images/[apod|eic|spacex]**. За данный функционал отвечают скрипты *fetch_nasa.py* и *fetch_spacex.py*. Также раз в сутки скрипт *main.py* с помощью телеграм-бота размещает все загруженные фотографии в канале t.me/tg_nasa_channel.


## Требования
* python-dotenv==0.20.0
* requests==2.22.0
* python-telegram-bot==20.0a0
* Наличие API-токена [NASA](https://api.nasa.gov/), который требуется разместить в файле *.env*

## Установка
```bash
git clone https://github.com/b3cch4/space_img.git
cd space_img/
python -m venv env && source env/bin/activate
pip install -r requirements.txt
echo API_KEY_NASA = your_api_key_from_NASA >> .env
echo API_BOT = your_api_for_telegram_bot >> .env
echo CHAT_ID = your_chat_id >> .env
```

## Настройка и запуск
По умолчанию фотогафия из раздела [APOD](https://api.nasa.gov/#apod) загружается ежедневно, но если раскомментировать строки 12 и 13 в файле *fetch_nasa.py*, заменив на диапазон чисел, можно получить фото за конкретный период времени.
```
'start_date': '2022-01-01', 
'end_date': '2022-02-01',
```
(данный интервал получает снимки за один месяц)

Программа имеет бесконечный цикл, в котором, изменяя время, можно изменять частоту выгрузку фотографий и публикации последних в [телеграм-канале](https://t.me/tg_nasa_channel)
```
time.sleep(86400)
```
(данный интервал запускает программу один раз в сутки)
