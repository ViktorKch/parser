import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}

base_url = 'http://www.tlock.ru/catalog/zamki_vreznye/dlya_legkikh_dverey/'

def lock_parser(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'prod__name'})
        for div in divs:
            content = div.contents
            print(content[-1].strip())

    else:
        print('ERROR')

lock_parser(base_url, headers)

