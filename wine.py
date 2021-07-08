import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random


def refined(s):
  r = s.split(':')[1]
  print(r)

headers = {
  "Host" : "winestyle.ru",
  "User-Agent" : user,
  "Accept": "*/*",
  "Accept-Encoding": "qzip, deflate, br",
  "Connection": "keep-alive"
  }

url = "https://winestyle.ru/wine/gruzvinprom/"
req = requests.get(url, headers=headers)

with open("sites.html", "w", encoding="utf-8") as file:
  file.write(req.text)

soup = BeautifulSoup(req.text, "lxml")
block = soup.find("div", {"class": "meta"})
artikul = block.find("span", class_= "bg-text").text
rating = refined(artikul)
#