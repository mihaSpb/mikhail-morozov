def max_number(a, b):
    return a if a > b else b


def empty_function():
    pass


def even_numbers(n):
  for number in range(0, n + 1, 2):
      yield number

def check_max_number():
    assert max_number(10, 5) == 10, "Ошибка: max_number(10, 5) должно возвращать 10"
    assert max_number(-1, -5) == -1, "Ошибка: max_number(-1, -5) должно возвращать -1"
    assert max_number(3.5, 7.2) == 7.2, "Ошибка: max_number(3.5, 7.2) должно возвращать 7.2"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должно возвращать 0"
    print("\nВсе автотесты для max_number пройдены успешно.")


print("Чётные числа: ", list(even_numbers(18)))
empty_function()
check_max_number()