import requests
from bs4 import BeautifulSoup
import fake_useragent

# Подстановка различных параметров браузера
user = fake_useragent.UserAgent().random

headers = {
  "Host" : "browser-info.ru",
  "User-Agent" : user,
  "Accept": "*/*",
  "Accept-Encoding": "qzip, deflate, br",
  "Connection": "keep-alive"
  }

url = "https://icanhazip.com/"
url1 = "https://browser-info.ru/"
req = requests.get(url1, headers=headers)
# print(req.text)
# print(req.status_code)

with open("ip.html", "w", encoding="utf-8") as file:
    file.write(req.text)


soup = BeautifulSoup(req.text, "lxml")
block = soup.find("div", id = "tool_padding")

# chek_js
chek_js = block.find("div", id = "javascript_check")
status_js = chek_js.find_all("span")[1].text
result_js = f"js: {status_js}"

# chek_flash
chek_fl = block.find("div", id = "flash_version")
status_fl = chek_fl.find_all("span")[1].text
result_fl = f"fl: {status_fl}"

# chek_br
result_br = block.find("div", id = "user_agent").text
print(result_br)
print(result_js)
print(result_fl)

