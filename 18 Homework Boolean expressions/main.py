age = int (input("Введите ваш возраст: "))
citizen = input("Являетесь ли вы гражданином страны? (да/нет): ").strip().lower()
disqualified = input("Есть ли у вас правовые ограничения, например не погашенная судимость? (да/нет): ").strip().lower()

is_citizen = (citizen == "да")
is_not_disqualified = (disqualified == "нет")

if age >= 18 and is_citizen and is_not_disqualified:
    print("Вы можете принять участие в голосовании!")
else:
    print("Вы не можете голосовать.")