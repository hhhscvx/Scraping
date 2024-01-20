import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def clean_data(strok):  # 1,153 total ratings
    r = strok.split()[0]
    r = r.replace(',', '')
    return r


def write_csv(data):
    with open('plugins.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow([data['name'],
                         data['url'],
                         data['reviews']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    featured = soup.find_all('section')[1]
    plugins = featured.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        reviews = clean_data(plugin.find('div', class_='plugin-rating').find('a').text)
        # print(f'"{name}" - {url}; Reviews: {clean_data(reviews)}')

        data = {'name': name,
                'url': url,
                'reviews': reviews}

        write_csv(data)

    # return plugins


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
