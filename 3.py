import requests  # парсинг криптовалют
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def clean_data(price):
    price = price.replace('.', '')
    price = price.replace(',', '.')
    return price


def write_csv(data):
    with open('coin.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        name = tds[2].find('a').text
        symbol = tds[3].text.strip()
        url = 'https://ru.investing.com' + tds[2].find('a').get('href')
        price = clean_data(tds[4].text)

        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price}

        write_csv(data)


def main():
    url = 'https://ru.investing.com/crypto/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
