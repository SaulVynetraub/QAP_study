# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#
# events = [
#     {
#         "timestamp": 159000,
#         "type": "ItemViewEvent",
#         "session_id": "qwe"
#     },
#     {
#         "timestamp": 158000,
#         "type": "ItemSearchEvent",
#         "session_id": "asd"
#     },
#     {
#         "timestamp": 157000,
#         "type": "ItemMakingEvent",
#         "session_id": "zxc"
#     }
# ]
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
#                       event_type=event.get("type"),
#                       session_id=event.get("session_id"))
#     print(event_obj.timestamp)
#
# import datetime
#
#
# class Product:
#     max_quantity = 100000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantiny_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantiny_in_stock > 0 else False
#
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.max_quantity)
# print(eggs.is_available())
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def getWidth(self):
#         return self.width
#
#     def getHeight(self):
#         return self.height
#
#     def getArea(self):
#         return self.width * self.height
#
#
# r1 = Rectangle(10, 5)
# print("r1.width=", r1.width)
# print("r1.height=", r1.height)
# print("r1.area=", r1.getArea())
#
# r2 = Rectangle(50, 20)
# print("r2.width=", r2.width)
# print("r2.height=", r2.height)
# print("r2.area=", r2.getArea())
#
#
# class Cat:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#
#     def cat_meow(self):
#         return "Meow! Meow!"
#
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_area(self):
#         return self.a * self.b
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_area_square(self):
#         return pow(self.a, 2)
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_area_circle(self):
#         return 3.14 * pow(self.r, 2)
#
#
# rect_1 = Rectangle(2, 3)
# rect_2 = Rectangle(20, 30)
# print(rect_1.get_area())
# print(rect_2.get_area())
#
# square_1 = Square(10)
# square_2 = Square(15)
# print(square_1.get_area_square())
# print(square_2.get_area_square())
#
# circle_1 = Circle(4)
# circle_2 = Circle(24)
# print(circle_1.get_area_circle())
# print(circle_2.get_area_circle())
#
# figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     elif isinstance(figure, Circle):
#         print(figure.get_area_circle())
#     else:
#         print(figure.get_area())