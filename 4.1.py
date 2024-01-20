import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    if not response.ok:
        print(response.status_code)
    return response.text


def write_csv(data):
    with open('4.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],
                         data['url'],
                         data['desc'],
                         data['review']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    sites_names = []
    sites_urls = []
    sites_descs = []
    sites_reviews = []
    sites = soup.find_all('div')[11]
    names = sites.find_all('p', class_='cat_result')
    for name in names:
        sites_names.append(name.text)
    urls = sites.find_all('p', class_='cat_result')
    for url in urls:
        sites_urls.append('http://katalogsajtov.ru' + url.find('a').get('href'))
    descs = sites.find_all('p', class_='cat_result3')
    for desc in descs:
        sites_descs.append(desc.text)
    reviews = sites.find_all('p', class_='cat_result2')
    for review in reviews:
        sites_reviews.append(review.text.split()[-1][1:-1])

    for i in range(len(sites_names)):
        data = {'name': sites_names[i],
                'url': sites_urls[i],
                'desc': sites_descs[i],
                'review': sites_reviews[i]}
        write_csv(data)


def main():
    for i in range(1, 4):
        url = f'http://katalogsajtov.ru/rabota/zarabotok-v-internete?p={i}'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
