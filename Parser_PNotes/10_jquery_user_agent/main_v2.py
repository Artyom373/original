# https://catertrax.com/why-catertrax/traxers/page/11/?themify_builder_infinite_scroll=yes
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
import csv
import requests
from bs4 import BeautifulSoup

def get_html(url):
    user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    r = requests.get(url, headers=user_agent)
    return r.text

def write_csv(data):
    with open("testi.csv", "a") as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts # [] or [a,b,s]

def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {'author': author, 'since': since}
        write_csv(data)


def main():
    # 1. Получения контейнера с отзывами и списка отзывов
    # 2. Если список есть, то парсим отзывы
    # 3. Если список пустой, то цикл прерывается
    page = 1
    while True:

        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/?themify_builder_infinite_scroll=yes'.format(str(page))

        articles = get_articles(get_html(url)) # [] or [1,2,3]

        if articles: # Если есть данные в арикле
            get_page_data(articles)
            page = page + 1
            print(url)
        else: # Если артиколь пустой
            break

if __name__ == "__main__":
    main()