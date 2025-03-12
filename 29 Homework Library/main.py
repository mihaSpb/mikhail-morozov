# Определение статуса книги: True == "в наличии", False == "выдана", None == "статус не определён"
def check_status(status):
    if status is True:
        return "в наличии"
    elif status is False:
        return "выдана"
    else:
        return "статус не определён"


def book_list_view(library):
    if library:
        print("\nСписок книг в библиотеке:")
        for title, info in library.items():
            status = info.get("наличие")
            # Используем функцию check_status для получения текстового описания статуса
            status_text = check_status(status)
            print(f"{title} - {status_text}")
    else:
        print("\nВ библиотеке нет книг.")


def add_book(library, title, author, year):
    new_book = {"автор": author, "год": year, "наличие": None}

    if title in library:
        answer = input(f"\nКнига '{title}' уже существует. Обновить информацию о ней? (Да/Нет): ").strip().lower()
        if answer == "да":
            library[title] = new_book
            print(f"Информация о книге '{title}' успешно обновлена.\n")
        else:
            print(f"Информация о книге '{title}' не обновлена.\n")
    else:
        library[title] = new_book
        print(f"Книга '{title}' успешно добавлена.\n")


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f"\nКнига '{title}' успешно удалена.\n")
    else:
        print(f"\nКнига '{title}' не найдена.\n")


# При выдаче книги устанавливает поле "наличие" в False
def issue_book(library, title):
    if title in library:
        library[title]["наличие"] = False
        status_text = check_status(library[title]["наличие"])
        print(f"Книга '{title}' успешно выдана. Текущий статус: {status_text}\n")
    else:
        print(f"Книга '{title}' не найдена.\n")


# При возврате книги устанавливает поле "наличие" в True.
def return_book(library, title):
    if title in library:
        library[title]["наличие"] = True
        print(f"Книга '{title}' успешно возвращена.\n")
    else:
        print(f"Книга '{title}' не найдена.\n")


# Поиск книги по названию и вывод информации о ней
def find_book(library, title):
    if title in library:
        print(f"\nИнформация о книге '{title}':")
        for key, value in library[title].items():
            if key == "наличие":
                print(f"статус: {check_status(value)}")
            else:
                print(f"{key}: {value}")
    else:
        print(f"\nКнига '{title}' не найдена.")


# Обработка выбранных пунктов пользовательского меню
def menu_add_book(library):
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    year = input("Введите год издания книги: ").strip()
    add_book(library, title, author, year)


def menu_remove_book(library):
    title = input("Введите название книги для удаления: ").strip()
    remove_book(library, title)


def menu_issue_book(library):
    title = input("Введите название книги для выдачи: ").strip()
    issue_book(library, title)


def menu_return_book(library):
    title = input("Введите название книги для возврата: ").strip()
    return_book(library, title)


def menu_find_book(library):
    title = input("Введите название книги для поиска: ").strip()
    find_book(library, title)


def menu_list_books(library):
    book_list_view(library)


# Пользовательское меню
def user_menu(library):
    menu = {
        "1": ("Добавить книгу", menu_add_book),
        "2": ("Удалить книгу", menu_remove_book),
        "3": ("Выдать книгу", menu_issue_book),
        "4": ("Вернуть книгу", menu_return_book),
        "5": ("Найти книгу", menu_find_book),
        "6": ("Показать список книг", menu_list_books),
        "0": ("Выход", None)
    }

    while True:
        print("\nМеню:")
        for key, item in menu.items():
            description = item[0]
            print(f"{key}. {description}")

        choice = input("Выберите опцию: ").strip()
        if choice == "0":
            print("Выход из программы.")
            break
        elif choice in menu:
            func = menu[choice][1]
            func(library)
        else:
            print("Неверный выбор, попробуйте снова.\n")


def main ():
    library = {
        "Война и мир": {"автор": "Лев Толстой", "год": 1869, "наличие": True},
        "Улисс": {"автор": "Джеймс Джойс", "год": 1921, "наличие": False},
        "Танец с драконами": {"автор": "Джордж Р. Р. Мартин", "год": 2011, "наличие": None},
        "Колыбель для кошки": {"автор": "Курт Воннегут", "год": 1963, "наличие": False},
        "Песчаные короли": {"автор": "Джордж Р. Р. Мартин", "год": 2005, "наличие": True}
    }

    user_menu(library)


main()