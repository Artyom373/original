import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s):
    # 1,470 total ratings
    r = s.split(' ')[0]   # 1,470  Преобразуем строку и разделяем ее пробелом, забираем 0 элемент
    return r.replace(',', '') # 1470 Заменяем запятую на пустоту

def write_csv(data):
    with open('plugins.csv', 'a') as f:  # a - записать в конец данные, w -перезаписывает
        writer = csv.writer(f)

        writer.writerow( [data['name'],
                         data['url'],
                         data['reviews']] ) # принимает только один аргумент из-за этого используем картеж "(" или список "["


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article') # 4

    for plugin in plugins:
        # [ plugin1, plugin2, plugin3, plugin4 ]
        name = plugin.find("h3").text
        url = plugin.find('h3').find('a').get('href')

        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating }

        # print(data)
        write_csv(data)



def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))



if __name__ == '__main__':
    main()
