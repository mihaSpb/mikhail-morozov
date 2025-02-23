my_string_with_space = "   Оттепель на улице вызывает ощущение приближающейся весны.   "
my_string_original = "Достигнуты договорённости по вопросу понижения ключевой ставки."
my_string_full = "Python is great"

my_string_list = ["P", "y", "t", "h", "o", "n", "i", "s", "g", "r", "e", "a", "t", "a", "g", "a", "i", "n"]
word1 = "".join(my_string_list[0:6])
word2 = "".join(my_string_list[6:8])
word3 = "".join(my_string_list[8:13])
word4 = "".join(my_string_list[13:])

result = " ".join([word1, word2, word3, word4])

print(my_string_with_space.strip())
print(my_string_original.replace("Достигнуты", "Не были достигнуты"))
print(my_string_full.split(" "))
print(result)