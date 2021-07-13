from bs4 import BeautifulSoup
import re


# .find()
# .find_all()

# .parent   Поиск родительского класса
# .find_parent() Посик родительского класса по условию

# .parents   Поиск родительских классов
# .find_parents() Поиск всех родительских классов

# .find_next_sibling() поиск соседних элементов с общими родителями
# .find_previous_sibling()

def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:    # Поиск элементов, содержащие слова Copywriter, если есть передаем tag
        return tag
    return None


def get_salary(s):
    # salary: 2700 usd per month
    pattern = r'\d{1,9}'
    # salary = re.findall(pattern, s)[0]  или этот метод
    salary = re.search(pattern, s).group() # или этот, они одинаковые
    print(salary)


def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')
    # row = soup.find_all('div', {'data-set': 'salary'})
    #
    # alena = soup.find('div', text='Alena').find_parent(class_='row')
    # print(alena)

    # copywriters = []
    #
    # persons = soup.find_all('div', class_='row')
    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append(cw)    Если есть информация в переменной cw то записываем в список copywriters
    #
    # print(copywriters)

    salary = soup.find_all('div', text=re.compile('\d{1,9}')) # текст где есть цифры
    for i in salary:
        print(i.text)

    # ^ - начало строки
    # $ - конец строки
    # . - любой символ
    # + - неограниченное количество вхождений
    # '\d' - цифра
    # '\w' - буквы, цифры, _
# Пример @tvitter искать ^@\w+







if __name__ == '__main__':
    main()
