import csv
from peewee import *


db = PostgresqlDatabase(database='parser', user='postgres', password='Boro1278', host='192.168.1.84') #Подключение к таблице

class Coin(Model):     #Описание таблицы с типами столбцов
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db



def main():

    db.connect() #Установка подключения
    db.create_tables([Coin]) # Создание таблицы Coin

    with open('cmc.csv') as f:
        order = ['name', 'url', 'price']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        # for row in coins:     #Первый способ загрузить в базу. Высокая загрузка HDD
            # coin = Coin(name=row['name'], url=row['url'], price=row['price'])
            # coin.save()

        with db.atomic():
            # for row in coins:               # Второй способ через транзакции. В 3 раза быстрее первого способа
            #     Coin.create(**row)
            for index in range(0, len(coins), 100):   # Третий способ по 100 индексов. В 20 раз быстрее чем первый способ
                Coin.insert_many(coins[index:index+100]).execute()


if __name__ == '__main__':
    main()
