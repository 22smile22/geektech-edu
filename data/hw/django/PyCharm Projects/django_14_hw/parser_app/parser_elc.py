#hw6
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://www.kompanion.kg/ru/retail/cards"
URL = "https://www.kompanion.kg/ru/retail/cards/elcard"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-md-8 col-md-push-4 xContent')
    card = []

    for item in items:
        card.append(
            {
                'title': item.find('div', class_='content').find('h1').get_text(),
                'image': HOST + item.find('div', class_='content').find('a', class_='thumb').
                    find('img', class_='uploaded').get('src')
            }
        )
        return card

@csrf_exempt
def parser_func_elc():
    html = get_html(URL)
    if html.status_code == 200:
        card = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            card.extend(get_data(html.text))
            return card
    else:
        raise ValueError('Permission denied')