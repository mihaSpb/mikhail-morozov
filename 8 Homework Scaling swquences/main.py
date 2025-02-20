
string_with_double_quotes = "Это строка с \"двойными кавычками\" внутри текста."

string_with_single_quotes = 'Это строка с \'одинарными кавычками\' внутри текста.'

string_with_backslash = "C:\\Users\\User\\Documents\\file.txt"

string_with_newline = "Это первая строка.\nЭто вторая строка."

string_with_tab = "Имя   \t  Фамилия\nАлексей\t  Петров"

multiline_string = """Это многострочная строка,
которая содержит "двойные кавычки", 'одинарные кавычки',
а также символы табуляции:\tПример табуляции
и символы новой строки,
которые сохраняют форматирование без экранирования символов."""

print(f"{string_with_double_quotes} \n")
print(f"{string_with_single_quotes} \n")
print(f"{string_with_backslash} \n")
print(f"{string_with_newline} \n")
print(f"{string_with_tab} \n")
print(f"{multiline_string}")