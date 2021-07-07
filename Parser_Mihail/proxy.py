import requests
import re

# Вытаскиеваем список прокси
with open("Parser_Mihail\proxy.txt") as file:
    proxy_base = "".join(file.readlines()).strip().split("\n")
# print(proxy_base)

# Пробегаем и добавляем в словрь
for proxy in proxy_base:
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    url = "https://icanhazip.com/"
    try:
        responce = requests.get(url, proxies=proxies, timeout=2).text
        print(f"IP:{responce}")
    except:
        print(f"ИП нерабочий")

