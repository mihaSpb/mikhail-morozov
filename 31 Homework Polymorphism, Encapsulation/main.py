class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Депозит: {amount}. Новый баланс: {self.__balance}")
        else:
            print("Неверная сумма для депозита!")


    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Снятие: {amount}. Новый баланс: {self.__balance}")
            else:
                print("Недостаточно средств для снятия!")
        else:
            print("Неверная сумма для снятия!")


    def get_balance(self):
        return self.__balance


def menu():
    account = BankAccount(0)

    actions = {
        "1": ("Положить на депозит", account.deposit),
        "2": ("Снять с депозита", account.withdraw),
        "3": ("Узнать баланс", account.get_balance),
        "4": ("Выйти", None)
    }

    while True:
        print("\nМеню:")
        for key, (description, _) in actions.items():
            print(f"{key}. {description}")

        choice = input("Выберите операцию: ")

        if choice == "4":
            print("Выход из программы.")
            break
        elif choice in actions:
            action = actions[choice][1]
            if action == account.get_balance:
                balance = account.get_balance()
                print("Текущий баланс:", balance)
            else:
                try:
                    amount = float(input("Введите сумму: "))
                except ValueError:
                    print("Неверный ввод. Пожалуйста, введите число.")
                    continue
                action(amount)
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    menu()
