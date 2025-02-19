# Сложение
print("1. Сложение")

try:
    num1 = float (input("Введите первое число: "))
    num2 = float (input("Введите второе число: "))
    result = num1 + num2
except ValueError:
    print("Ошибка! Пожалуйста, введите числовое занчение!")
else:
    print(f"Результат сложения: {result}\n")


# Вычитание
print("2. Вычитание")

try:
    num1 = float (input("Введите первое число: "))
    num2 = float (input("Введите второе число: "))
    result = num1 - num2
except ValueError:
    print("Ошибка! Пожалуйста, введите числовое занчение!")
else:
    print(f"Результат вычитания: {result}\n")


# Умножение
print("3. Умножение")

try:
    num1 = float ( input("Введите первое число: "))
    num2 = float ( input("Введите второе число: "))
    result = num1 * num2
except ValueError:
    print("Ошибка! Пожалуйста, введите числовое занчение!")
else:
    print(f"Результат умножения: {result}\n")


# Деление
print("4. Деление")

try:
    num1 = float ( input("Введите первое число: "))
    num2 = float ( input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Ошибка! Пожалуйста, введите числовое занчение!")
except ZeroDivisionError:
    print("Ошибка! Деление на ноль!")
else:
    print(f"Результат деления: {result}")