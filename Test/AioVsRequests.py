import os
import time
import random
import requests
import cfscrape
import asyncio
from aiocfscrape import CloudflareScraper
from time import perf_counter
from bs4 import BeautifulSoup


SITE = "https://thispersondoesnotexist.com/image"
IMAGES_COUNT = 50
URL_DAILY = "https://yandex.ru/maps-reviews-widget/1112802767?comments"
URL_FULL = "https://yandex.ru/maps/org/1112802767/reviews/"
URL_ADRESS = "https://yandex.ru/maps/172/ufa/house/ulitsa_rikharda_zorge_66_2/YU8YdgZjTEYEQFtufXt3eX1iYg==/?ll=56.013534%2C54.768116&z=17"
# PROXY = "12.155.121.214:8000"
HEADERS = {
    'Host': 'yandex.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


async def get_async_session(url):
    async with CloudflareScraper() as session:
        async with session.get(url) as resp:
            print(resp)
            return await resp.text()


def get_sync_session():
    session = requests.Session()
    session.headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'viewport-width': '1920'
    }
    return cfscrape.create_scraper(sess=session)


def sync_extracter():
    response = get_sync_session().get(URL_FULL, proxies=None)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # extension = response.headers["content-type"].split('/')[-1]


def async_extracter():
    response = asyncio.run(get_async_session(URL_ADRESS))
    soup = BeautifulSoup(response, 'html.parser')
    print(soup)


if __name__ == "__main__":
    start_sync = perf_counter()
    print(URL_FULL)
    sync_extracter()
    print(f"time: {(perf_counter() - start_sync):.02f}")
    start_async = perf_counter()
    
    print(f"time: {(perf_counter() - start_async):.02f}")
