def book_list_view(library):
    if library:
        print("Список книг в библиотеке:")
        for title in library:
            print(title)
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


def main ():
    library = {
        "Война и мир": {"автор": "Лев Толстой", "год": 1869, "наличие": "в наличии"},
        "Улисс": {"автор": "Джеймс Джойс", "год": 1921, "наличие": "выдана"},
        "Колыбель для кошки": {"автор": "Курт Воннегут", "год": 1963}
    }

    book_list_view(library)
    add_book(library, "Улисс", "Джеймс Джойс", 1921)
    book_list_view(library)

    remove_book(library, "Колыбель для кошки")
    book_list_view(library)


main()