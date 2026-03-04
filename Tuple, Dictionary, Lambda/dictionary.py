print("Робота із словниками (dictionaries)")
# у .NET словник називається Dictionary, у Python - dict
# Словник - це набір елементів - ключ значення. При цьому ключ не може повторитися
student = {
    "name": "Іван Марков",
    "age": 20,
    "grade": 95
};

print(student);

print(student["name"]);
print(student.get("name"));

# Додавання елемента до словника
student["email"] = "ivan.markov@example.com";
print(student);

# Видалення елемента зі словника
del student["grade"];
print(student);

# перебір елементів словника
for key in student:
    print(f"{key}: {student[key]}");