num = int(input("Введите число от 1 до 5: "))

num_to_word = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}

if num in num_to_word:
    print(num_to_word[num])
else:
    print("Ошибка: введите число от 1 до 5")