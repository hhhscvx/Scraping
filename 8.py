import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('websites.csv', 'a') as file:
        order = ['name', 'url', 'desc', 'traffic', 'percent']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def main():
    """parsing ajax; Вкратце: открыли dev tools -> network -> xhr -> click on next page -> go to xhr request -> check url"""
    for i in range(0, 300):  # всего 3713 страниц но возьму 300 чтоб не жрать время
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={str(i)}'
        response = get_html(url)
        data = response.strip().split('\n')[1:]

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


if __name__ == '__main__':
    main()
