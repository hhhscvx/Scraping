import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find(
        'table', class_='table table-striped table-bordered').find_all('tr')[1:11]

    proxies = []

    for tr in trs:
        tds = tr.find_all('td')

        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        scheme = 'https' if 'yes' in tds[6].text.strip() else 'http'
        proxy = {'scheme': scheme, 'address': f"{ip}:{port}"}
        proxies.append(proxy)

    return choice(proxies)


def get_html(url):
    # proxies = {'https': 'ipaddress:5000'}
    p = get_proxy()  # {'sheme': '', 'address': ''}
    proxy = {p['scheme']: p['address']}
    r = requests.get(url, proxies=proxy, timeout=5)
    return r.json()['origin']


def main():
    url = 'https://httpbin.org/ip'
    print(get_html(url))


if __name__ == '__main__':
    main()
