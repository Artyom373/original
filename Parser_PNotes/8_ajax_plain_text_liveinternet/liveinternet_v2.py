import requests
import csv
from requests.adapters import HTTPAdapter    # Библиотека для избежания блока
from requests.packages.urllib3.util.retry import Retry # Библиотека для избежания блока


def get_html(url):

    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=0.5) #Применяется задержка между запросами и 5 попытки в случ. ошибки
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    r = session.get(url)
    return r.text


def write_csv(data):
    with open('websites.csv', 'a', encoding='utf-8') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def main():

    for i in range(0, 5708):
        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
        response = get_html(url)
        data = response.strip().split('\n')[1:]  # Взяли строку через strip убрали лишние пробелы, через split разделили строку на  список
        # [1:] ,берет все без первого элемента ( первый элемент это 0)

        for row in data:
            columns = row.strip().split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            write_csv(data)






if __name__ == '__main__':
    main()
