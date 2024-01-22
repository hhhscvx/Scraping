import csv
from peewee import *


db = PostgresqlDatabase(database='test', user='postgres',  # from peewee
                        password='05081992', host='localhost')


class Coin(Model):  # from peewee, ebat это короче модели из django
    name = CharField()
    symbol = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db


def main():

    db.connect()
    db.create_tables([Coin])

    with open('coin.csv') as file:
        order = ['name', 'symbol', 'url', 'price']  # соотв. полям в Coin(Model)
        reader = csv.DictReader(file, fieldnames=order)

        coins = list(reader)

        # for row in coins:  # плохой способ сохранения в БД
        #     coin = Coin(name=row['name'], symbol=row['symbol'],
        #                 url=row['url'], price=row['price'])
        #     coin.save()

    with db.atomic():
        for row in coins:  # хороший способ
            Coin.create(**row)

        # чтобы не каждый коин записывать, а разбивать по 100 штук и записывать (лучший способ)
        # for index in range(0, len(coins), 100):
        #     Coin.insert_many(coins[index:index+100]).execute()

    # В завершении вынесение БД в файл: pg_dump -U postgres(имя юзера) -h localhost(имя хоста) test(имя БД) > coins.sql (в PycharmProjects/Scraping)


if __name__ == '__main__':
    main()
