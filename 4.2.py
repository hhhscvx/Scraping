"""hueta ne rabotaet"""


import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text if response.ok else print(response.status_code)


def clean_data(strok):
    res = strok.replace(',', '').replace('$', '')
    return res


def write_csv(data):
    with open('4.2.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],
                         data['tiker'],
                         data['url'],
                         data['price']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[2].find('div').find('div').find(
                'div').find('div').find('p').text
        except:
            name = ''
        try:
            tiker = tds[2].find('div').find('div').find(
                'div').find('div').find('div').find('p').text
        except:
            tiker = ''
        try:
            url = 'https://coinmarketcap.com' + \
                tds[2].find('div').find('a').get('href')
        except:
            url = ''
        try:
            price = clean_data(tds[3].find('div').find('a').text)
        except:
            price = ''
        # print(f'{name} - {tiker}; {url}; price - {price}')
        data = {'name': name, 'tiker': tiker, 'url': url, 'price': price}
        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'

    while True:
        get_page_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')
        try:
            url = 'https://coinmarketcap.com/' + \
                soup.find('ul', class_='pagination').find(
                    'li', class_='next').find('a').get('href')
        except:
            break


if __name__ == '__main__':
    main()
