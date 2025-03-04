def sum_even_numbers():
    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number
    return total

def odd_squares():
    squares = [x * x for x in range(1, 11) if x % 2 != 0]
    return squares

def count_numbers_until_negative():
    count = 0
    while True:
        try:
            number = float(input("Введите число (отрицательное число для завершения): "))
        except ValueError:
            print("Ошибка: введите корректное число.")
            continue
        if number < 0:
            break
        count += 1
    return count

def main():
    even_sum = sum_even_numbers()
    print("Сумма всех четных чисел от 1 до 100:", even_sum)

    squares = odd_squares()
    print("Квадраты нечетных чисел от 1 до 10:", squares)

    count = count_numbers_until_negative()
    print("Количество введенных чисел:", count)


main()