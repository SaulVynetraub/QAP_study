array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
any_number = int(input("Введите любое число: "))


def array_high(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array_high(array)

print(f"Вывод отсортированной последовательности: {array}.")


def find_binary(array, any_number, left, right):
    if left > right:
        return f"Введенное число {any_number} отсутствует в последовательности."

    middle = (right + left) // 2
    if array[middle] == any_number:
        return middle
    elif any_number < array[middle]:
        return find_binary(array, any_number, left, middle - 1)
    else:
        return find_binary(array, any_number, middle + 1, right)


print(find_binary(array, any_number, 0, len(array)))
