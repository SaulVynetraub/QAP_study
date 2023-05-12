def add_2_plus_2():
    result = 2 + 2
    print(result)


add_2_plus_2()


def hello_world():
    print("hello world!")


hello_world()


def delitel(n, a):
    if a % n == 0:
        print(f"{n} является делителем числа {a}.")
    else:
        print(f"{n} не является делителем числа {a}.")


delitel(5, 12)


def stairs(n):
    for i in range(n, 0, -1):
        print("*" * i)


stairs(8)


def pow_func(base, n=2):
    inside_result = base ** n
    return inside_result


outside_result = pow_func(3)
print(outside_result)


def count_delitel(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    return (count)


print(count_delitel(127))


def test(string):
    string = string.lower()
    string = string.replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False


print(test("Кит на море не романтик"))


def mul(*nums):
    p = 1
    for n in nums:
        p = p * n

    return p


print(mul(1, 2, 3, 4, 5))


def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


print(sum(20))


def sum_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digit(n // 10)


print(sum_digit(123))


def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


for num in fib():
    print(num)


def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step


def repeat_list(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value


for i in repeat_list([1, 2, 3]):
    print(i)


def twice_func(inside_func):
    inside_func()
    inside_func()


def hello():
    print("hello")


test = twice_func(hello)
print(test)


def make_adder(x):
    def adder(n):
        return x + n

    return adder


add_5 = make_adder(5)
print(add_5(10))
print(add_5(100))


def linear_solve(a, b):
    if a:
        return b / a
    elif not a and not b:  # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else:
        return "Нет корней"


def D(a, b, c):
    return b ** 2 - 4 * a * c


def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return "Нет вещественных корней"
    elif D(a, b, c) == 0:
        return -b / (2 * a)
    else:
        return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)


L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))


def positive(x):
    return x % 2 == 0


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
print(list((result)))

a = ["это", "маленький", "текст", "обидно"]
list(map(str.upper, a))


def my_decor(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, *kwargs)

    return wrapper


@my_decor
def say_word(word):
    print(word)


print(say_word("Oo!!!"))


def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result

    return wrapper