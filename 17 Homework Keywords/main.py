def max_number(a, b):
    result = (a + b + abs(a - b)) / 2
    assert result >= a and result >= b
    return result


def empty_function():
    pass


def even_numbers(n, current = 0):
    try:
        assert current <= n
        yield current
        yield from even_numbers(n, current + 2)
    except AssertionError:
        return


assert max_number(10, 5) == 10, "Ошибка: max_number(10, 5) должно возвращать 10"
assert max_number(-1, -5) == -1, "Ошибка: max_number(-1, -5) должно возвращать -1"
assert max_number(2.5, 8.8) == 8.8, "Ошибка: max_number(2.5, 8.8) должно возвращать 8.8"
assert max_number(100, 200) == 200, "Ошибка: max_number(100, 200) должно возвращать 200"
assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должно возвращать 0"

print("\nВсе автотесты для max_number пройдены успешно.\n")

print(list(even_numbers(18)))

empty_function()