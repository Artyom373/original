import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text
  #  print(dir(r)) dir Выводит все параметры функции :'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'

def main():
    url = "https://wordpress.org/"
    print(get_h1(get_html(url)))

def get_h1(html):
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.find("div", id="home-welcome").find("header").find("h1").text
    return h1

if __name__ == "__main__":
    main()