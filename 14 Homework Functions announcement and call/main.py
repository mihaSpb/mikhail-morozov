def say_hello():
    print("Hello, Python!")

def repeat_message(message, count):
    result = (message + "\n") * count
    print(result, end= "")


say_hello()
repeat_message("Сообщение для повтора", 3)