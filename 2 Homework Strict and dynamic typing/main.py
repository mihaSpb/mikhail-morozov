# Strict typing
a = 5
b = "890"

result = a + int(b)
print(type(result))


s = "abc"
try:
    result = int(s)
except ValueError:
    print("Error: ValueError невозможно преобразовать строку 'abc' в целое число.")


# Dynamic typing
num = 42
print(type(num))

num = "String"
print(type(num))


