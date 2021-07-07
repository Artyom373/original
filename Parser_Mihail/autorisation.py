import requests
from bs4 import BeautifulSoup
import fake_useragent
# https://forum.ruboard.ru/
# vb_login_username
# vb_login_password
# Ссылка на форум
link = "https://forum.ruboard.ru/login.php?do=login"
# Ссылка на профиль
profil = "https://forum.ruboard.ru/member.php/496651-artyom373373"
# Подставляет рандомный браузер
user = fake_useragent.UserAgent().random
session = requests.Session()
headers = {
  "Host" : "forum.ruboard.ru",
  "User-Agent" : user,
  "Accept": "*/*",
  "Accept-Encoding": "qzip, deflate, br",
  "Connection": "keep-alive"
  }

# Данные для входа на форум
data = {
    "vb_login_username" : "artyom373373",
    "vb_login_password" : "16knkyeKU"
    }

# Авторизация на форуме
rec = session.post(link, data=data, headers=headers).text

# Получение куков в словарь
cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
    for key in session.cookies
    ]

# Использование куков, которые получили ранее
session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)

# Получение страницы профиля
profil_rec = session2.get(profil, headers=headers).text
print(profil_rec)