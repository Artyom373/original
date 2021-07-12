import requests
from bs4 import BeautifulSoup
import csv

def get_html(html):
    r = requests.get(html)
    if r.ok:
        return r.text
    print(r.status_code)

def refined(s):
    r = s.replace('$', '')
    r = r.replace(',', '')
    return r

def write_csv(data):
    with open("cms.csv", "a", encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow((data["name"], data["price"]))

def get_page_data(html):
    soup = BeautifulSoup(html, "lxml")
    trs = soup.find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[2].find("div", display="flex").find("p").text
            price = tds[3].find('a').text
            price = refined(price)
        except:
            name = tds[2].find_all("span")[1].text
            price = tds[3].find('span').text
            price = refined(price)
        data = {'name': name,
                'price': price}

        write_csv(data)

def pages(html):
    soup = BeautifulSoup(html, "lxml")
    page = soup.find("ul", class_="pagination").find_all("li")[-2].find("a").text
    return int(page)
def main():
    url = "https://coinmarketcap.com/"
    page = pages(get_html(url))
    pattern = "https://coinmarketcap.com/?page={}"
    for i in range(0, page+1):
        url = pattern.format(str(i))
        get_page_data(get_html(url))
if __name__ == "__main__":
    main()
