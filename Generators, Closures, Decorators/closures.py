def my_view_message(msg):
    message = msg[0:9]
    def private_func():
        print(message)
    return private_func

closure = my_view_message("Hello World!")
closure() #Викликаємо вказівник на метод, який є в середині