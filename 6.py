from bs4 import BeautifulSoup
import re


# .find()
# .find_all()

# .parent()
# .find_parent()

# .find_next_sibling() - поиск соседей в блоке (братья и сестры)
# .find_previous_sibling()

def get_copywriter(tag):  # получение из persons копирайтеров
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def get_salary(s):
    # salary: 2700 usd per month
    pattern = r'\d{1, 9}'  # \d - цифра, \d{1, 9} - все цифры от 1 до 9
    salary = re.findall(pattern, s)[0]  # re.findall(<что ищем>, <где ищем>)


def main():
    """Методы BeautifulSoup"""
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')

    # аналог class_=row, имба при data-set`ах
    row = soup.find_all('div', {'class': 'row'})

    # родительский контейнер (контейнера с текстом 'Какой-то текст div`а')
    text = soup.find('div', text='Какой-то текст div`а').parent
    # text = soup.find('div', text='Какой-то текст div`а').find_parent(class_='row') - конкретизация поиска родителя

    copywriters = []

    persons = soup.find_all('div', class_='row')
    for person in persons:
        cw = get_copywriter(person)
        if cw:
            copywriters.append(cw)

    # еще вариант - soup.find_all('div', text=re.compile('\d{0-9}')) - div`ы у которые в тексте есть цифры
    salary = soup.find_all('div', {'data-set': 'salary'})
    for i in salary:
        print(i.text.strip())

    # re:
    # ^ - начало строки
    # $ - конец строки
    # . - любой символ
    # + - неограниченное кол-во вхождений
    # '\d' - цифра
    # '\w' - буква/цифра/_


if __name__ == '__main__':
    main()
