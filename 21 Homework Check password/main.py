password = "password"

while True:
    user_input = input("Введите пароль: ")
    if user_input == password:
        print("Пароль верный!")
        break
    else:
        print("Неверный пароль, попробуйте снова!")
