from notes.classes import Car  # импорт класса Car из модуля (файла) classes.py

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from notes.classes import Electric_Car as EC  # импорт класса ElectricCar с алиасом

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

from notes.classes import Car, Electric_Car  # импорт классов Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = Electric_Car('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())

from notes import classes

my_beetle = classes.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = classes.Electric_Car('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())