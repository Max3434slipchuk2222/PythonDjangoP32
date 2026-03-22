from datetime import datetime
#1
def myfunction(first, last):
    for i in range(first, last+1):
        if i % 2 == 0:
            yield i

print("Парні числа:")
for item in myfunction(1, 10):
    print(item, end="\t")
#2
def myfunction2(first, last, numbers):
    for i in range(first, last+1):
        if i in numbers :
            yield i
numbers = [1, 20, 44, 4, 450, 3, 8, 19, 35, 14, 23, 56]
print("Усі числа що входять в заданий діапазаон:")
for item in myfunction2(1, 18, numbers):
    print(item, end="\t")
#3
def is_even(n):
    return n % 2 == 0
def is_odd(n):
    return n % 2 != 0
def check_number(value_to_check, function_to_call):
    return function_to_call(value_to_check)
number = int(input("\nВведіть число: "))
choice = input("Виберіть на що перевіряти (1 - парність, 2 - непарність): ")
if choice == "1":
    result = check_number(number, is_even)
    task = "парність"
else:
    result = check_number(number, is_odd)
    task = "непарність"
if result:
    print(f"Число {number} пройшло перевірку на {task}")
else:
    print(f"Число {number} не пройшло перевірку на {task}")
#4

def first_decorator(func):
    def wrapper():
        print("***************************")
        func()
        print("***************************")
    return wrapper
def display_time():
    time = datetime.now()
    print(time.strftime("%H:%M"))
decorated_time = first_decorator(display_time)
decorated_time()
#5
def second_decorator(func):
    def wrapper():
        print("+++++++++++++++++++++")
        func()
        print("+++++++++++++++++++++")
    return wrapper

second_decorated = second_decorator(decorated_time)
second_decorated()
#6
def third_decorator(func):
    def wrapper(*args, **kwargs):
        print("***************************")
        result = func(*args, **kwargs)
        print("***************************")
        return result
    return wrapper
@third_decorator
def display_time():
    time = datetime.now()
    print(time.strftime("%H:%M"))
display_time()
#2.1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def prime_numbers(first, last):
    for i in range(first, last+1):
        if is_prime(i):
            yield i

print("Прості числа:")
for item in prime_numbers(1, 100):
    print(item, end="\t")
#2.2
def is_armstrong(n):
    string = str(n)
    power = len(string)

    total_sum = 0
    for digit in string:
        total_sum += int(digit) ** power

    return total_sum == n
def armstrong_numbers(first, last):
    for i in range(first, last + 1):
        if is_armstrong(i):
            yield i
print("\nЧисла Армстронга:")
for item in armstrong_numbers(1, 500):
    print(item, end="\t")
#2.3
def get_min(a, b):
    return a if a < b else b
def get_max(a, b):
    return a if a > b else b


def find_min_or_max(list_to_check, function_to_call):
    result = list_to_check[0]

    for i in range(1, len(list_to_check)):
        result = function_to_call(result, list_to_check[i])

    return result

numbers = [1, 20, 44, 4, 450, 3, 8, 19, 35, 14, 23, 56]
print("\n", numbers)
choice = input("Виберіть що знайти в списку (1 - максимум, 2 - мінімум): ")
if choice == "1":
    res = find_min_or_max(numbers, get_max)
    print(f"Максимальне число: {res}")
else:
    res = find_min_or_max(numbers, get_min)
    print(f"Мінімальне число: {res}")
#2.4
def pizza():
    return "Основа (тісто та соус)"
def margarita(func):
    def wrapper():
        return func() + " + томати + моцарела + базилік"
    return wrapper
def hawaiian(func):
    def wrapper():
        return func() + " + шинка + ананас"
    return wrapper
@margarita
def make_margarita():
    return pizza()
@hawaiian
def make_hawaiian():
    return pizza()
print(f"Піцца Маргарита: {make_margarita()}")
print(f"Піцца Гавайська: {make_hawaiian()}")