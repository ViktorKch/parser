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
    list = soup.find_all(class_='prod__link block-link clearfix')
    for a in list:
        product_link = 'http://www.tlock.ru' + a['href']
        secondary_html = get_html(product_link)
        product_soup = BeautifulSoup(secondary_html, 'html.parser')
        descriptions = product_soup.find_all('div', attrs={'id': 'description'})
        for description in descriptions:
            decr = description.contents
            print(decr[0])


main()