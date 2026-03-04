print("Робота з анонімними функціями")
# на .NET це делегати, в Python це анонімні функції
# lambda - це ключове слово для створення анонімної функції
# синтаксис: lambda аргументи: вираз

square = lambda x: x * x # піднести число до квадрата
print(square(5)) # 25

# def - це ключове слово для створення іменованої функції
def my_square(x):
    return x*x

print(my_square(5)) # 25
# масив обєктів студентів
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]
# відсортувати студентів за віком
# Цей мутує
# students.sort(key=lambda student: student["age"])
# print(students) # [{'name': 'Alice', 'age': 20}, {'name

sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students) # [{'name': 'Alice', 'age': 20}, {'name

#показати тип для першого студента
print(type(students[0])) # <class 'dict'>