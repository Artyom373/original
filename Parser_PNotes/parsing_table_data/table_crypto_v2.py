import requests
from bs4 import BeautifulSoup
import csv
import fake_useragent

user = fake_useragent.UserAgent().random
headers = {
  "Host" : "coinmarketcap.com",
  "User-Agent" : user,
  "Accept": "*/*",
  "Accept-Encoding": "qzip, deflate, br",
  "Connection": "keep-alive"
  }
def refined(s):
    r = s.replace('$', '')
    r = r.replace(',', '')
    return r

def get_html(url):
    r = requests.get(url, headers=headers)
    return r.text

def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']])

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[2].find("div", display="flex").find("p").text
            symbol = tds[2].find("div", display="flex").find_all('p')[1].text
            url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
            price = tds[3].find('a').text
            price = refined(price)
        except:
            name = tds[2].find_all("span")[1].text
            symbol = tds[2].find_all("span")[2].text
            url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
            price = tds[3].find('span').text
            price = refined(price)
        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price}

        write_csv(data)

def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))

if __name__ == '__main__':
    main()
