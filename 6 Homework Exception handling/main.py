try:
    num1 = float ( input("Введите первое число: "))
    num2 = float ( input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Ошибка! Пожалуйста, введите числовое занчение!")
except ZeroDivisionError:
    print ("Ошибка: Деление на ноль!")
else:
    print("Результат операции деления: { result }")
finally:
    print("Программа деления завершена")