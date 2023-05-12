class Dog():  # создание класса Dog
    def __init__(self, name,
                 age):  # обязательный метод init с обязательным self и необязательными параметрами (аргументами)
        self.name = name
        self.age = age

    def sit(self):  # задание первого метода (функции), что делает экземпляр класса
        print(f"{self.name} is now sitting.")

    def roll_over(self):  # задание второго метода
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)  # создание первого экземпляра класса Dog
print(f"My dog's name is {my_dog.name}.")  # вывод значения параметра "имя"
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()  # вызов первого метода "сидеть"
my_dog.roll_over()  # вызов второго метода "перекатиться"

your_dog = Dog('Lucy', 3)  # создание второго экземпляра
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()


class Car:  # создание класса Car
    def __init__(self, make, model, year):  # self, необязательные параметры "изготовитель", "модель", "год"
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # задание базового значения параметра пробега

    def get_descriptive_name(self):  # метод для вывода полного описания автомобиля
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):  # метод для вывода значения пробега
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):  # метод для обновления (ввода нового) значения пробега
        if mileage >= self.odometer_reading:  # запрещает понизить значение пробега
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # метод для приращения пробега
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', '2019')  # создание первого экземпляра класса Car
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 30
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_used_car = Car('subaru', 'outback', 2015)  # создание второго экземпляра
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


class Battery():  # создание класса Battery для описания электромобиля
    def __init__(self, battery_size=75):  # задание базового значения параметра емкости аккумулятора
        self.battery_size = battery_size

    def get_range(self):  # метод для определения запаса хода
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def describe_battery(self):  # метод для вывода емкости аккумулятора
        print(f"This car has a {self.battery_size}-kWh battery.")


class Electric_Car(Car):  # создание класса-преемника ElectricCar (электромобиля) от класса-родителя Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # применение методов класса-родителя к преемнику
        self.battery = Battery()

    def fill_gas_tank(self):  # игнорирование метода класса-родителя (либо замена его действия)
        print("This car doesn't need a gas tank!")


my_tesla = Electric_Car('tesla', 'model s', 2019)  # создание экземпляра класса ElectricCar
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()