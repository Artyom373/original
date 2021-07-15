import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open("websit1.csv", "a", encoding='utf-8') as f:
        order = ['name', 'url', 'descriptions', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def main():
    for i in range(0, 10):
        url = "https://www.liveinternet.ru/rating/ru//today.tsv?page={}".format(str(i))
        response = get_html(url)
        data = response.strip().split("\n")[1:]
        for row in data:
            colums =row.strip().split("\t")
            name = colums[0]
            url = colums[1]
            descriptions = colums[2]
            traffic = colums[3]
            percent = colums[4]

            data = {
            "name": name,
            "url": url,
            "descriptions": descriptions,
            "traffic": traffic,
            "percent": percent
            }
            write_csv(data)







if __name__ == "__main__":
    main()