import os

import cfscrape
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

API_YAM_TOKEN = os.getenv('API_YAM_TOKEN')
TEXT_KEY = os.getenv('TEXT_KEY')
YAM_ID = os.getenv('YAM_ID')


def get_count_star(review_stars):
    star_count = 0
    for review_star in review_stars:
        if '_empty' in review_star.get('class'):
            continue
        elif '_half' in review_star.get('class'):
            star_count = star_count + 0.5
        else:
            star_count = star_count + 1
    return star_count


def get_session():
    session = requests.Session()
    session.headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'viewport-width': '1920'
    }
    return cfscrape.create_scraper(sess=session)


def parsing_day(data_result, r):
    result = {
        'company_reviews': []
    }
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        reviews = soup.find_all('div', {"class": "comment"})
    except:
        return None
    for r in reviews:
        try:
            review_name = r.find('p', {"class": "comment__name"}).text
        except:
            review_name = None
        try:
            review_date = r.find('p', {"class": "comment__date"}).text
        except:
            review_date = None
        try:
            review_text = r.find('p', {"class": "comment__text"}).text
        except:
            review_text = None
        try:
            star_count = get_count_star(
                r.find('ul', {"class": "stars-list"})
            )
        except:
            star_count = None
        if review_name is not None:
                result['company_reviews'].append({
                    'author': review_name,
                    'data_time': review_date,
                    'text': review_text,
                    'mark': star_count
                })
    return result


def day_extracter(yandex_id=YAM_ID):
    url = 'https://yandex.ru/maps-reviews-widget/' + str(yandex_id) + '?comments'
    print(url)
    session = get_session()
    r = session.get(url)
    print(r)
    data_result = {
        'company_reviews': []
    }
    data_result = parsing_day(data_result, r)
    return data_result


if __name__ == '__main__':
    result = day_extracter()
    print(*result.values())
    # for _ in result:
    #     print(_)

    # print(*result.values())
    # with open('company_reviews.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)
    print('Parsing Success')
    