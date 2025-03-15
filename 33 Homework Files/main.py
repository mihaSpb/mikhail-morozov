def main():
    with open("data.txt", "w", encoding = "utf-8") as file:
        file.write("Это первая строка текста.\n")
        file.write("Это вторая строка текста.\n")
        file.write("Это третья строка текста.\n")


    print("Содержимое файла data.txt:")
    with open("data.txt", "r", encoding = "utf-8") as file:
        content = file.read()
        print(content)


    with open("data.txt", "a", encoding = "utf-8") as file:
        file.write("Это четвертая строка текста (добавлена).\n")
        file.write("Это пятая строка текста (добавлена).\n")


    print("Содержимое файла data.txt построчно:")
    with open("data.txt", "r", encoding = "utf-8") as file:
        for line in file:
            print(line, end = "")


    source_file = "data.txt"
    dest_file = "data_copy.txt"
    with open(source_file, "rb") as src:
        data = src.read()
    with open(dest_file, "wb") as dst:
        dst.write(data)

    print(f"\nФайл {source_file} успешно скопирован в {dest_file}.")


if __name__ == "__main__":
    main()
