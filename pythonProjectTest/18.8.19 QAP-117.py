how_many = int(input("Сколько билетов приобретаете? "))
result = []
for person in range(how_many):
    age = int(input("Укажите возраст посетителя: "))
    if age < 18:
        price = 0
        print("Билет бесплатный.")
    elif 18 < age < 25:
        price = 990
        print(f"Цена билета: {price} руб.")
    elif age > 25:
        price = 1390
        print(f"Цена билета: {price} руб.")
    result.append(price)
purchase = sum(result)
if how_many <= 3:
    print(f"Полная стоимость заказа: {purchase} руб.")
else:
    print(f"Стоимость заказа с учетом скидки 10%: {0.9 * purchase} руб.")
