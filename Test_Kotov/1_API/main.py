import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

responseHello = requests.get("https://playground.learnqa.ru/api/get_text")
print(responseHello.text)