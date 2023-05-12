text = open('JesusOfSuburbia.txt')  # открытие текстового файла в директории проекта
print(text.read())  # вывод всего содержимого файла строкой
print(text.readline(20))  # вывод 20 символов первой строки файла
print(text.readline(20))  # вывод 20 символов второй строки
print(text.readlines())  # вывод всего содержимого файла списком с элементами-строками
for line in text:  # чтение файла построчно через цикл
    print(line)

my_file = open('new_file.txt', 'w')  # создание нового текстового файла для записи
my_file.write('Hello!')  # запись строки в текстовый файл
print('World', file=my_file)  # второй вариант записи

with open('new_file.txt') as my_file:  # открытие текстового файла с присвоением алиаса
    for letter in my_file:
        print(letter)  # после выполнения кода происходит автоматическое закрытие файла

myFile = open(r'C:\Users\Админ\Desktop\test\filename.txt', 'rt',
              encoding="utf8")  # абсолютный путь файла вне директории проекта;
# rt - открыт на чтение в текстовом режиме; utf8 - кодировка для разбора кириллицы
path_1 = open(r'C:\Users\Админ\Desktop')  # команда cd в терминале, переход к папке выше по уровню
path_1 = open(r'test\filename.txt')  # вызов файла
path_2 = open(r'C:\Users\Админ\Desktop_1\test_other')  # нахождение в соседней папке
path_2 = open(r'..\test\filename.txt')  # вызов файла; ..\ - подняться на уровень выше

import json  # вызов модуля json

with open('json_example.json', encoding='utf8') as f:  # открытие json-файла
    templates = json.load(f)  # load - метод из модуля, представляет файл как словарь

print(templates)
print(type(templates))

with open('json_example.json', encoding='utf8') as f:
    strfile = f.read()  # запись содержимого файла json в строку
    templates = json.loads(strfile)  # преобразование строки в словарь

template = {}  # словарь в Python
with open('to_json_example.json', 'w', encoding='utf8') as f:
    json.dump(template, f, ensure_ascii=False,
              indent=4)  # запись словаря Python в файл формата json; сохранение кириллицы и удобной записи;
    # template - словарь, f - файл json под запись
with open('to_json_example.json', encoding='utf8') as f:
    print(f.read())

with open('numbers.txt') as file_object:  # чтение файла в каталоге проекта
    contents = file_object.read()  # сохранение содержимого файла в переменную
print(contents.rstrip())

with open(r'C:\Users\ld135\Desktop\numbers.txt') as file:  # чтение файла по абсолютному пути
    number = file.read()
print(number)

file = 'numbers.txt'
with open('numbers.txt') as file:  # чтение файла по строкам
    for line in file:
        print(line.rstrip())  # удаление символа новой строки (\n)

file = 'numbers.txt'
with open('numbers.txt') as file:
    lines = file.readlines()  # сохранение переменной и использование вне блока with
for line in lines:
    print(line.rstrip())

file = 'numbers.txt'
with open('numbers.txt') as file:
    lines = file.readlines()
num_string = ''
for line in lines:
    num_string += line.strip()  # удаление пробелов между строками
print(num_string)
print(len(num_string))

file = 'program.txt'
with open(file, 'w') as file_writing:  # запись в файл с перезаписью содержимого
    file_writing.write("I love programming.\n")
    file_writing.write("I love creating new games.\n")

file_name = 'program.txt'
with open(file_name, 'a') as file_object:  # запись в файл с добавлением
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.")

import json

numbers = [1, 3, 5, 8, 9]
filename = 'numbers.json'
with open(filename, 'w') as f:  # создание списка в файле с расширением .json
    json.dump(numbers, f)  # запись списка numbers в файл filename как f

import json

filename = 'numbers.json'
with open(filename) as f:  # чтение списка из json-файла
    numbers = json.load(f)
print(numbers)

import json

username = input("What is your name? ")  # сохранение имени, введенного пользователем
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

import json

with open(filename) as f:
    username = json.load(f)  # чтение сохраненного имени из json-файла
    print(f"Welcome back, {username}!")

import json


def greet_user():  # функция приветствия с исключением: если файл с именем не будет найден, запросит ввод имени
    """Приветствует пользователя по имени."""
    filename = 'username_1.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)  # запись нового имени в файл
            print(f"We will remember you when you come back, {username}!")
    else:  # выполняется, если файл будет найден
        print(f"Welcome back, {username}!")


greet_user()

import json


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username_2.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username  # используется в функции greet_user в блоке if, если файл будет найден


def get_new_username():
    """Запрашивает имя нового пользователя."""
    username = input("What's your name? ")
    filename = 'username_2.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username  # используется в функции greet_user в блоке else


def greet_user():  # приветствует, если изначально файл (с сохраненным именем) был найден
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()