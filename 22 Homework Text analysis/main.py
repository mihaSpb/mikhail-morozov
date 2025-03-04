import re

# Текст к нижнему регистру и удаление знаков препинания.
def clean_input_text(text):
    re.sub(r"[^\w\s]", "", text.lower())

# Разбивка очищенного текста на список слов
def get_words(text):
    return text.split()

# Возвращает количество слов в списке
def count_words(words):
    return len(words)

# Определение самого длинного слова в списке
def get_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Подсчёт гласных
def count_vowels(text):
    vowels = set("аеёиоуыэюя")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Подсчёт сколько раз слово встречается в списке
def get_word_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def print_results(word_count, longest_word, vowel_count, word_freq):
    print("Количество слов в тексте:", word_count)
    print("Самое длинное слово:", longest_word)
    print("Количество гласных букв в тексте:", vowel_count)
    print("Частота встречаемости слов:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

def main():
    text = input("Введите текст: ")

    cleaned_text = clean_input_text(text)
    words = get_words(cleaned_text)

    word_count = count_words(words)
    longest_word = get_longest_word(words)
    vowel_count = count_vowels(cleaned_text)
    word_freq = get_word_frequency(words)

    print_results(word_count, longest_word, vowel_count, word_freq)


main()