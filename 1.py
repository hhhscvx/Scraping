import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='siteSub').text
    return h1


def main():
    url = 'https://ru.wikipedia.org/wiki/Python/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
