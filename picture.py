from bs4 import BeautifulSoup
from urllib.request import *

url = "http://www.tlock.ru/catalog/zamki_vreznye/dlya_legkikh_dverey/"



def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find_all(class_='prod__img')
    for a in list:
        secondary_html = a['src'].split('/')[-1]
        urlretrieve('http://www.tlock.ru/photo_bank/'+secondary_html, secondary_html)
        print(secondary_html + ': скачан')

main()
