from bs4 import BeautifulSoup
import re

def get_copywriter(tag):
    whois = tag.find("div", id="whois").text.strip()
    if "Copywriter" in whois:
        return tag
    return  None

def get_salary(s):
    # salary: 2700 usd per month
    pattern = r'\d{1,9}'
    # salary = re.findall(pattern, s)[0] или этот метод
    salary = re.search(pattern, s).group()  # или этот метод, они одинаковые
    print(salary)


def main():
    file = open("index.html", encoding='utf-8').read()
    soup = BeautifulSoup(file, "lxml")
    # alena = soup.find("div", text="Alena").find_parent(class_="row")
    # print(alena)


    # copywriters = []
    # personal = soup.find_all("div", class_="row")
    # for person in personal:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append((cw))
    # print(copywriters)

    salary = soup.find_all("div", {"data-set": "salary"})
    for i in salary:
        get_salary(i.text)



if __name__ == "__main__":
    main()