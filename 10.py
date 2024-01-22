import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    user_agent = {  # без юзерагента сервер не пускал, скопировали его из Network -> xhr -> response -> Headers -> User-Agent
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(data):
    with open('testimonials.csv', 'a') as file:
        order = ['author', 'since']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    reviews = soup.find(
        'div', class_='testimonial-container').find_all('article')
    return reviews  # [] or [a, b, c...]


def get_page_data(reviews):
    for review in reviews:
        try:
            since = review.find('p', class_='traxer-since').text.strip().split()[-1]
        except:
            since = ''
        try:
            author = review.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''

        data = {'author': author, 'since': since}
        write_csv(data)


def main():
    while True:
        page = 1
        url = f'https://catertrax.com/traxers/page/{str(page)}/'

        articles = get_articles(get_html(url))

        if articles:
            get_page_data(articles)
            page = page + 1
        else:
            break


if __name__ == '__main__':
    main()
