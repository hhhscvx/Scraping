"""ne rabotaet ofc"""
import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r

def write_csv(data):
    with open('videos.csv', 'a') as file:
        order = ['name', 'url']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['content_html']

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find('div', id='content')

    for item in items:
        name = item.find('a', id='video-title-link').get('title')
        url = 'https://youtube.com' + \
            item.find('a', id='video-title-link').get('href')

        data = {'name': name, 'url': url}
        write_csv(data)


def get_next(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['load_more_widget_html']
    
    soup = BeautifulSoup(html, 'lxml')

    try:
        url = 'https://youtube.com' + soup.find('button', class_='load-more-button').get('data-uix-load-more-href')
    except:
        url = ''

    return url


def main():
    url = 'https://www.youtube.com/@bmchn/videos'
    get_page_data(get_html(url))

    while True:
        response = get_html(url)
        get_page_data(response)
        
        url = get_next(response)

        if url:
            continue
        else:
            break


if __name__ == '__main__':
    main()
