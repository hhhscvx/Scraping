import requests
import csv
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('websites.csv', 'a') as file:
        order = ['name', 'url', 'desc',
                  'traffic', 'percent']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_data(text):
    data = text.strip().split('\n')[1:]

    for row in data:
        cols = row.strip().split('\t')
        name = cols[0]
        url = cols[1]
        desc = cols[2]
        traffic = cols[3]
        percent = cols[4]
        data = {'name': name,
                'url': url,
                'desc': desc,
                'traffic': traffic,
                'percent': percent}
        write_csv(data)


def make_all(url):
    text = get_html(url)  # парсинг страницы
    get_data(text)  # запись в csv


def main():
    # 2665
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 400)]

    with Pool(20) as p:
        # для каждого урла выполнить парсинг страницы и запись в csv
        p.map(make_all, urls)


if __name__ == '__main__':
    main()
