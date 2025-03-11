# Изменения для отображения статуса книги: True == "в наличии", False == "выдана", None == "статус не определён"
def book_list_view(library):
    if library:
        print("Список книг в библиотеке:")
        for title, info in library.items():
            status = info.get("наличие")
            if status is True:
                status_text = "в наличии"
            elif status is False:
                status_text = "выдана"
            else:
                status_text = "статус не определён"
            print(f"{title} - {status_text}")
    else:
        print("В библиотеке нет книг.")


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


# При выдаче книги устанавливает поле "наличие" в False.
def issue_book(library, title):
    if title in library:
        library[title]["наличие"] = False
        print(f"Книга '{title}' успешно выдана.\n")
    else:
        print(f"Книга '{title}' не найдена.\n")


# При возврате книги устанавливает поле "наличие" в True.
def return_book(library, title):
    if title in library:
        library[title]["наличие"] = True
        print(f"Книга '{title}' успешно возвращена.\n")
    else:
        print(f"Книга '{title}' не найдена.\n")


def main ():
    library = {
        "Война и мир": {"автор": "Лев Толстой", "год": 1869, "наличие": True},
        "Улисс": {"автор": "Джеймс Джойс", "год": 1921, "наличие": False},
        "Танец с драконами": {"автор": "Джордж Р. Р. Мартин", "год": 2011, "наличие": None},
        "Колыбель для кошки": {"автор": "Курт Воннегут", "год": 1963, "наличие": False},
        "Песчаные короли": {"автор": "Джордж Р. Р. Мартин", "год": 2005, "наличие": True}
    }

    book_list_view(library)
    add_book(library, "Улисс", "Джеймс Джойс", 1921)
    book_list_view(library)

    remove_book(library, "Война и мир")
    book_list_view(library)

    issue_book(library, "Песчаные короли")
    return_book(library, "Улисс")
    book_list_view(library)

main()