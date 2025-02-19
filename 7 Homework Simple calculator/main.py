
try:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    operation = int (input("Введите номер операции (1/2/3/4): "))

    num1 = float (input("Введите первое число: "))
    num2 = float (input("Введите второе число: "))

    if operation == 1:
        result = num1 + num2
        typeOperation = "сложения"
    elif operation == 2:
        result = num1 - num2
        typeOperation = "вычитания"
    elif operation == 3:
        result = num1 * num2
        typeOperation = "умножения"
    elif operation == 4:
        result = num1 / num2
        typeOperation = "деления"

except ValueError:
    print("Ошибка! Пожалуйста, введите числовое занчение!")

except ZeroDivisionError:
    print("Ошибка! Деление на ноль!")

else:
    print(f"\nРезультат {typeOperation}: {result}")