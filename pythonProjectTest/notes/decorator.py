"""Декоратор для дублирования кортежа значений, возвращаемого основной функцией original_function."""


def my_decorator(any_function):
    print("\tНачало декорирования функции.")

    def wrapper(*args, **kwargs):
        print("Получение аргументов из основной функции. Имеем кортеж из двух значений: (max a, min b).")
        tuple_1 = 2 * any_function(*args, **kwargs)
        print("После дублирования:")
        return (f"Результат работы декоратора: {tuple_1}.")

    return wrapper


@my_decorator
def original_function(*lists):
    return max(*lists), min(*lists)


print(original_function([1, 2, 3, 4]))