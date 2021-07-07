import requests
from bs4 import BeautifulSoup
import fake_useragent

images_number = 0 #Имя файла
storege_number = 1 #Номер страницы
link = f"https://zastavok.net"

for storage in range(2476): #Цикл на изменению номера страницы
    responce = requests.get(f"{link}/{storege_number}").text   #Парсинг ссылки со страницей
    soup = BeautifulSoup(responce, "lxml")
    block = soup.find("div", class_ = "block-photo") #Получение всего блока с каринками
    all_image = block.find_all("div", class_ = "short_full") #Парсинг всех блоков с каринками по отдельности

# Посмотреть все блоки
# for images in all_image:
#     print(images)
#     print("\n\n")

    for images in all_image:
        href = images.find("a").get("href") #Получение ссылки с картинкой
        download_starage = requests.get(f"{link}/{href}").text #Парсинг ссылки с картинкой
        download_soup = BeautifulSoup(download_starage, "lxml")
        # Получения ссылки на саму картинку
        dowload_block = download_soup.find("div", class_ = "image_data").find("div", class_ = "block_down" )
        result_link = dowload_block.find("a").get("href")
    # Скачка картинок
        images_bytes = requests.get(f"{link}{result_link}").content
        with open(f"images/{images_number}.jpg", "wb") as file:
            file.write(images_bytes)
        images_number += 1
        print(f"{images_number}.jpg Успешно скачено")

    storege_number += 1