# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return (f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.")
#
#
# rect = Rectangle(5, 10, 50, 100)
# print(rect)
#
#
# class Rectangle_1:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_area(self):
#         return (f"The area of this rectangle-object is {self.x * self.y}.")
#
#
# rect_1 = Rectangle_1(30, 15)
# print(rect_1.get_area())
#
#
# class Client:
#     def __init__(self, firstname, lastname, city, balance=''):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.city = city
#         self.balance = balance
#
#     def information(self):
#         return (f"We have the next information about client:\n{self.firstname} {self.lastname}. {self.city}. "
#                 f"Баланс: {self.balance} руб.")
#
#     def __str__(self):
#         return f"{self.firstname} {self.lastname}. {self.city}. Баланс: {self.balance} руб."
#
#     def only_information(self):
#         return (f"{self.firstname} {self.lastname}, {self.city}.")
#
#
# client_1 = Client("Иван", "Петров", "Москва", 10000)
# print(client_1)
#
# clients = [
#     {
#         "firstname": "Ivan",
#         "lastname": "Ivanov",
#         "city": "Moscow"
#     },
#     {
#         "firstname": "Petr",
#         "lastname": "Petrov",
#         "city": "Saint-Petersburg"
#     },
#     {
#         "firstname": "Stepan",
#         "lastname": "Stepanov",
#         "city": "Stepanovsk"
#     }
# ]
#
# clients_for_party = []
# for client in clients:
#     even_client = Client(firstname=client.get("firstname"),
#                          lastname=client.get("lastname"),
#                          city=client.get("city"))
#     clients_for_party.append(client)
#
# print(f"This is the list of clients: {clients_for_party}.")
#
#
# # или
#
# def get_guest(self):
#     return f'{self.firstname} {self.lastname}, г. {self.city}.'
#
#
# customer_1 = Client('Иван', 'Петров', 'Москва', 50)
# customer_2 = Client('Владимир', 'Зайцев', 'Кострома', 50)
# customer_3 = Client('Олеся', 'Янина', 'Новосибирск', 50)
#
# guest_list = [customer_1, customer_2, customer_3]
#
# for guest in guest_list:
#     print(guest.get_guest())