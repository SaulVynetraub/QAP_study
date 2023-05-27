# spiski
one = ['one', 'two', 'three', 'four']  # zadanie spiska
print(one[3].title())  # obraw k tretiemu
print(one[-2])  # obraw k 2 s konca
friends = ['Ivan', 'Vlad', 'Alexandr', 'Slava', 'Margarita']
print(friends[-1])  # vivod poslednego v spiske
print(friends[0])  # vivod pervogo v spiske
friends[-1] = 'Nikita'  # zamena poslednego v spiske na novoe
friends.append('Dmitriy')  # dobavlenie novogo v konec
cats = []  # clear spisok, prosto metka!
cats.append('black')  # dobavl po odnomu
cats.append('white')
cats.append('brown')
cats.insert(2, 'grey')  # dobavlenie novogo na poz 2
del cats[1]  # udalenie "belogo" iz spiska bezvozvratno
popped_cat = cats.pop()  # udalenie poslednego s zapominaniem
first_cat = cats.pop(0)  # to je, no poz 0
books = ['Marabou Stork Nightmares', 'Hell Angels', 'White Whale', 'Filth']
books.remove('Filth')  # udalenie po znacheniy
deleted = 'White Whale'
books.remove(deleted)  # udalenie peremennoi
price = ['low', 'expensive', 'middle']
price.sort()  # sort po alfavitu v odnom registre
price.sort(reverse=True)  # sort v obratnom alfavitnom poryadke
cars = ['lamborgini', 'maserati', 'bmv', 'toyota', 'mersedes']
print(sorted(cars))  # vremennaya sort spiska, original sohranyaetsya
cars.reverse()  # zapis` spiska v obrat poryadke navsegda (s "mersedes")
cars.reverse()  # reverse obratno (v na4alo)
print(len(cars))  # dlina spiska

# rabota so spiskami
mags = ['alice', 'david', 'carolina']
for mag in mags:  # zadanie cycle for
    print(mag)
for value in range(5):  # spisok 4isel
    print(value)
numbers = list(range(1, 6))  # avtom sozd spiska
numb = list(range(2, 11, 2))  # spisok 4etnih 4isel ot 2 do 10]
squares = []  # pustoi spisok
for value in range(1, 11):
    square = value ** 2  # vozved value v kvadrat
    squares.append(square)  # dobavlyaet value v spisok squares []
print(squares)  # ili
square = []
for value in range(1, 11):
    square.append(value ** 3)
print(square)
digits = square  # statistika po spisku
print(min(digits))
print(max(digits))
print(sum(digits))
box = [value ** 2 for value in range(2, 22)]  # generator spiska
print(box)
players = ['charles', 'marina', 'sergey', 'artem', 'tamara']  # vivod 4asti spiska (segmenta)
print(players[3:])
for player in players[:-2]:  # vivod 2 ot konca spiska
    print(player.title())
print(players[:])
my_foods = ['pizza', 'falafel', 'cake']
friend_food = my_foods[:]  # copy s ispolz segmenta
my_foods.append('tomato')
friend_food.append('ice cream')
dimensions = (200, 50)  # korteji - neizmen spisok
print(dimensions[0])
for dimension in dimensions:
    print(dimension)
dim = (100, 20)  # zamena elementov v korteje
dim = (25, 500)

# operator if, elif, else
cars = ['bmw', 'audi', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'audi'  # prisvaivanie znach 'car'
if car == 'audi':  # proverka ravenstva
    print(car)
food = 'mushrooms'
if food != 'anchovies':  # proverka neravenstva
    print('Hold the anchovies!')
clear = 17
if clear != 42:  # proverka neravenstva 4isel v uslovii
    print('This is not true code!')
age_1 = 18
age_2 = 21
if age_1 <= 20 and age_2 <= 20:  # proverka istinnosti 2 uslovii srazu
    print('The humans are alive!')
age_2 = 17
if (age_1 <= 20) and (age_2 <= 20):
    print('Now is the currect form')
prime_1 = 2000
prime_2 = 1500
if prime_1 > 1800 or prime_2 > 1800:  # operator ili (ili/ili)
    print('I can buy this notebook!')
toppings = ['onions', 'mushrooms', 'apples']
if 'onions' in toppings:  # proverka nalichiya v spiske
    print('We have it!')
banned = ['andrew', 'carolina', 'matthew']
user = 'denis'
if user not in banned:  # proverka otsutstviya v spiske
    print(f"{user.title()}, you can write on this forum!")
book_1 = 'BOOK'
book_2 = 'book'
if book_1 == (f'{book_2.upper()}'):  # proverka s registrom
    print('This is a good book!')
num_1 = 26
num_2 = 33
if sum([num_1] + [num_2]) < 60:  # proverka summi po usloviu <
    print('True')
one = 10 ** 2
two = 50 * 2
if (one == 100) and two == 100:  # proverka usloviya and
    print('True')
temp_1 = 6 / 11
temp_2 = 99 - 94
if (temp_1 == 5) or (temp_2 == 5):  # proverka usloviya or
    print('True')
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('You are not old enough to vote(')
alias = 22  # zadanie neskolkih uslovii i rezultatov (if-elif-else)
if alias < 4:
    print('Your admission cost is $0.')
elif alias < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')
# ili
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'Your admission cost is ${price}.')
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:  # dop uslovie (dop elif)
    price = 40
else:
    price = 20
print(f'Your admission cost is ${price}.')
age = 64  # proverka na 1 uslovie
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:  # bez else
    price = 20
print(f'Your admission cost is ${price}.')
toppings = ['extra cheese', 'pepperoni']
if 'extra cheese' in toppings:  # proverka neskol`kih obyazat uslovii 4erez if
    print('Adding extra cheese.')
if 'pepperoni' in toppings:
    print('Adding pepperoni.')
if 'mushrooms' in toppings:
    print('Adding mushrooms.')
print('\nFinished making your pizza!')
toppings = ['mushrooms', 'green peppers', 'extra cheese']
for top in toppings:
    if top == 'extra cheese':  # esli net konkr elementa
        print(f'Sorry, we dont have a {toppings[2]} now.')
    else:
        print(f'Adding {top}.')
print('\nFinished making your pizza!')
roots = []
if roots:
    for root in roots:  # proverka na pustoi spisok
        print(f'Adding {roots}.')
    print('\nFinished making your pizza!')
else:
    print('\nAre you sure you want a plain pizza?')
avail_top = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
required_top = ['mushrooms', 'french fries', 'extra cheese']
for topping in required_top:
    if required_top in avail_top:  # proverka nalichiya elementa v drugom spiske
        print(f'Adding {required_top}.')
    else:
        print(f'Sorry, we dont have {required_top}.')
print('\nFinished making your pizza!')

# Dictionary
alien_0 = {'color': 'green', 'points': 5}  # zadanie slovarya
print(alien_0['color'])  # vivod znacheniya klucha 1
print(alien_0['points'])  # vivod znacheniya klucha 2
alien_0['x_pos'] = 0  # dobavlenie novih k/v
alien_0['y_pos'] = 25
new_points = alien_0['points']
alien_1 = {}  # zadanie pustogo slovarya
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['color'] = 'yellow'  # zamena znacheniya slovarya
alien_2 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}  # primer
print(f"Original position: {alien_2['x_pos']}")
alien_2['speed'] = 'fast'  # zamena znacheniya v slovare
if alien_2['speed'] == 'slow':
    x_incr = 1
elif alien_2['speed'] == 'medium':
    x_incr = 2
else:
    x_incr = 3
alien_2['x_pos'] = alien_2['x_pos'] + x_incr
print(f"New position: {alien_2['x_pos']}")
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']  # udalenie pari k/v
alien_3 = {'color': 'red', 'speed': 'slow'}
# get - prisvaivanie znacheniya po umolchaniy, esli net klucha v slovare
point_value = alien_3.get('points', 'No point value assigned.')
print(point_value)
languages = {  # slovar s odnotip znacheniyami
    'jen': 'python',
    'marina': 'c',
    'jonh': 'python',
    'phil': 'c++',
}
language = languages['phil'].title()
print(f"Phil`s favourite language is {language}.")
user_0 = {
    'username': 'efermi',
    'firstname': 'enrico',
    'lastname': 'fermi',
}
for k, v in user_0.items():  # perebor po param k/v
    print(f"\nKey: {k}")
    print(f"Value: {v}")
for k, v in user_0.items():
    print(f'His {k} is {v.title()}')
languages = {
    'jen': 'python',
    'marina': 'c',
    'jonh': 'python',
    'phil': 'c++',
}
friends = ['phil', 'jen']
for name in languages.keys():  # perebor po k (keys mojno opustit)
    print(f"Hi {name.title()}")  # vivod vseh k
    if name in friends:  # sravnivaet so spiskom
        language = languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")
if 'erin' not in languages.keys():  # proverka, est ili net v slovare
    print('Erin, please take our poll!')
languages = {
    'jen': 'python',
    'marina': 'c',
    'jonh': 'python',
    'phil': 'c++',
}
for name in sorted(languages.keys(), reverse=True):  # perebor i vivod k po alfavitu v obratnom poryadke
    print(f"{name.title()}, thank you for taking the pool.")
print('The following languages have been mentioned:')
for language in languages.values():  # perebor i vivod v
    print(language.title())
for language in set(languages.values()):  # vivod unikalnih v, zadanie mnojestva
    print(language.title())
languages = {'ruby', 'python', 'c', 'c++', 'python'}  # vivod mnojestva (unik v)
print(languages)
alien_0 = {'color': 'red', 'points': 5}
alien_1 = {'color': 'green', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(aliens)
aliens_0 = []  # pustoi spisok dlya 30 priwelcev
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}  # k/v
    aliens_0.append(new_alien)  # nadobavlyat v aliens_0
for alien in aliens_0[0:3]:  # dlya pervih 3:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens_0[0:5]:  # s 1 po 5
    print(alien)
print('...')
print(f"Total number of aliens: {len(aliens_0)}")  # podschet dliny spiska
pizza = {
    'crust': 'thick',  # strokovie v
    'toppings': ['mushrooms', 'extra cheese'],  # v spiskami
}
print(f"You ordered a {pizza['crust']}-crust pizza"
      " with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")  # ili ("\t" + topping)
languages = {
    'jen': ['python', 'ruby'],  # neskolko otvetov
    'sarah': ['javascript'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in languages.items():
    if len(languages) == 1:  # esli dlina spiska = 1
        print(f"\n{name.title()}`s favourite language is {languages[0].title()}")
    else:
        print(f"\n{name.title()}`s favourite language are:")
        for language in languages:
            print(f"\t{language.title()}.")
users = {  # slovar v slovare
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# while/input
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:  # poka cat v spiske pets
    pets.remove('cat')  # udalyat cat
print(pets)
unconf_users = ['alice', 'brian', 'david']  # neproveren
conf_users = []  # proveren
while unconf_users:  # poka v spiske ostaytsya elementi
    curr_user = unconf_users.pop()  # izvlech polzovatelya s konca spiska
    print(f"Verifying user: {curr_user.title()}")
    conf_users.append(curr_user)
print("\nThe following users have been confirmed:")
for conf_user in conf_users:
    print(conf_user.title())
question = "\nTell me something:"  # vpisat quit, chtobi ostanovit programmu
question += "\nEnter 'quit' to end the program."
active = True  # zadanie flaga
while active:  # poka flag = true
    message = input(question)  # zaprawivat slovo
    if message == 'quit':  # esli slovo = quit
        active = False  # menyaet flag
    else:
        print(message)
responses = {}
active = True  # flag prodoljeniya oprosa
while active:
    name = input("\nWhat is your name? ")  # zapros imeni
    response = input("Which mountain would you like to climb someday? ")  # zapros otveta
    responses[name] = response  # sohranenie otveta v slovare, prisvaivanie kluchu "name" znacheniya "response"
    repeat = input("Would you like to let another person respond? (Yes/No) ")  # proverka prodoljenya oprosa
    if repeat == 'No':
        active = False
print("\n--- Poll Results ---")  # opros zaverwen
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
question = "\nPlease enter the name of a city you have visited:"
question += "\n(Enter 'quit' when you are finished.)"
while True:  # vipoln beskonechno do "break"
    city = input(question)
    if city == 'quit':
        break  # esli goroda zakonch = ostanovit programmu
    else:
        print(f"I'd love to go to {city.title()}!")
    current = 0
while current < 10:
    current += 1  # current = current + 1
    if current % 2 == 0:  # esli delitsya na 2 bez ostatka
        continue  # vernutsya k nachalu
    print(current)
x = 1
while x <= 5:
    print(x)
    x += 1  # bez etogo daet 1, 1, 1 bez konca

name = input("Please, enter your name: ")
print(f"Hello, {name}!")
answer = "If you tell us who you are, we can personalize the messages you see."
answer += "\nWhat is your first name?"
name = input(answer)
print(f"\nHello, {name}!")
height = input("How tall are you, in inches?: ")
height = int(height)  # preobrazuet stroku v chislo
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
number = input("Enter a number: ")  # proverka na chet/nechet
number = int(number)
if number % 2 == 0:  # delitsya na 2 bez ostatka (==0)
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
current = 1  # perebor chisel, poka ne dostignet 5
while current < 5:
    print(current)
    current += 1
