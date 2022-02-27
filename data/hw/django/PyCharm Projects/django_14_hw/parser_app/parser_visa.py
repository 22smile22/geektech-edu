#hw6
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://cards.optimabank.kg/"
URL = "https://cards.optimabank.kg/corporate-cards.html"

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
    items = soup.find_all('div', class_='row-fluid card-info')
    card = []

    for item in items:
        card.append(
            {
                'title': item.find('div', class_='offset1 span8').find('span', class_='caption').
                    find('a').get_text(),
                'image': item.find('div', class_='span3').find('div', class_='card-img')
                    .find('a').find('img').get('src')
            }
        )
        return card

@csrf_exempt
def parser_func_visa():
    html = get_html(URL)
    if html.status_code == 200:
        card = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            card.extend(get_data(html.text))
            return card
    else:
        raise ValueError('Permission denied')