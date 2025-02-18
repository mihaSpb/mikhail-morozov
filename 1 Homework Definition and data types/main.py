x = 5
y = 3.14
z = "890"
my_list = [x, y, z]
my_tuple = {y, z, x}
my_dict = {"cat_name": "Tom", "cat_color": "grey"}
my_set = {"cats", "dogs", "turtles"}


print("Типы данных", type(x), type(y), type(z), type(my_list), type(my_tuple), type(my_dict), type(my_set))


print("Строка в целое число", int(z))

print("Число в строку", str(y))

print("Список в кортеж", tuple(my_list))

new_list = [x]
print("Целое число в список", new_list)