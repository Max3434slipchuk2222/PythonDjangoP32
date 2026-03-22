def my_decorator(func):
    def private_decorator():
        print("Ми декоруємо метод зелений світлофор")
        func()
        print("Червоне світло газу")
    return private_decorator

@my_decorator
def hello_message():
    print("hello world")

hello_message()