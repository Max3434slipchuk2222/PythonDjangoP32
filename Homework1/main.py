def basketball_menu():
    players = {
        "Майкл Джордан": 198,
        "Леброн Джеймс": 206
    }
    while True:
        print("Меню:")
        print("1. Вивести всіх баскетболістів")
        print("2. Додати баскетболіста")
        print("3. Видалити баскетболіста")
        print("4. Знайти баскетболіста")
        print("5. Змінити дані")
        print("0. Вихід")

        choice = input("Оберіть дію: ")
        if choice == "1":
            for name, height in players.items():
                print(f"{name}: {height} см")
        elif choice == "2":
            try:
                name = input("Введіть ПІБ: ")
                if name in players:
                    print("Такий гравець уже наявний")
                else:
                    height = int(input("Введіть зріст: "))
                    players[name] = height
                    print("Успішно додано")
            except ValueError:
                print("Ви ввели некоректне значення росту")

        elif choice == "3":
            name = input("Вкажіть ім'я для видалення: ")
            if name in players:
                del players[name]
                print(f"Гравця {name} видалено")
            else:
                print("Гравця не знайдено")

        elif choice == "4":
            name = input("Введіть ім'я для пошуку: ")
            if name in players:
                print(f"Зріст гравця {name}: ", players.get(name))
            else:
                print("Гравця не знайдено")

        elif choice == "5":
            name = input("Введіть ім'я для зміни: ")
            if name in players:
                new_height = int(input("Введіть новий зріст: "))
                players[name] = new_height
                print("Дані успішно оновлено")
            else:
                print("Гравця не знайдено")

        elif choice == "0":
            break
        else:
            print("Невірний вибір")

def dictionary_menu():
    words = {
        "hello": "bonjour",
        "bye": "salut"
    }
    while True:
        print("Англо-французький словник:")
        print("1. Показати всі слова")
        print("2. Додати слово")
        print("3. Видалити слово")
        print("4. Пошук перекладу")
        print("5. Змінити переклад")
        print("0. Вихід")

        choice = input("Оберіть дію: ")
        if choice == "1":
            for eng, fr in words.items():
                print(f"{eng} - {fr}")
        elif choice == "2":
            eng = input("Введіть англійське слово: ").lower()
            if eng in words:
                print("Слово вже є у словнику")
            else:
                fr = input("введіть французький переклад: ").lower()
                words[eng] = fr
                print("Успішно додано")
        elif choice == "3":
            eng = input("Вкажіть слово для видалення: ").lower()
            if eng in words:
                del words[eng]
                print(f"Слово {eng} видалено")
            else:
                print("Слово не знайдено")
        elif choice == "4":
            eng = input("Введіть слово для пошуку: ").lower()
            if  eng in words:
                print(f"Переклад слова {eng}: ", words.get(eng))
            else:
                print("Слово не знайдено")
        elif choice == "5":
            eng = input("Вкажіть слово для зміни ").lower()
            if eng in words:
                words[eng] = input("Введіть новий переклад: ").lower()
                print("Успішно оновлено")
            else:
                print("Не знайдено")
        elif choice == "0":
            break


def firma_menu():
    workers = {
        "Сліпчук Максим Юрійович": {"phone": "111111", "email": "max@mail.com", "posada": "Programmer", "room": "112", "skype": "max15_it"}
    }
    while True:
        print("Керування персоналом: ")
        print("1. Показати весь персонал")
        print("2. Додати робітника")
        print("3. Видалити робітника")
        print("4. Пошук робітника")
        print("5. Змінити робітника")
        print("0. Вихід")

        choice = input("Дія: ")
        if choice == "1":
            for name, info in workers.items():
                print(f"{name}: Тел: {info['phone']}, Посада: {info['posada']}")
        elif choice == "2":
            name = input("Введіть ПІБ: ")
            if name in workers:
                print("Данний робітник вже існує")
            else:
                workers[name] = {
                    "phone": input("Введіть телефон: "),
                    "email": input("Введіть email: "),
                    "posada": input("Введіть посада: "),
                    "room": input("Введіть кабінет: "),
                    "skype": input("Введіть skype: ")
                }
        elif choice == "3":
            name = input("Введіть ПІБ для видалення ")
            if name in workers:
                del workers[name]
                print(f"Робітника {name} видалено")
            else:
                print("Робітника не знайдено")
        elif choice == "4":
            name = input("Введіть ПІБ для пошуку: ")
            info = workers.get(name)
            if info:
                for k, v in info.items(): print(f"{k}: {v}")
            else:
                print("Не знайдено")
        elif choice == "5":
            name = input("Введіть ПІБ для зміни: ")
            if name in workers:
                workers[name]["phone"] = input("Введіть новий номер телефона")
                workers[name]["email"] = input("Введіть новий email")
                workers[name]["posada"] = input("Введіть нову посаду")
                workers[name]["room"] = input("Введіть нову кімнату")
                workers[name]["skype"] = input("Введіть новий skype")
                print("Успішно оновлено")
            else:
                print("Не знайдено")
        elif choice == "0":
            break


def books_menu():
    library = {
        "Кобзар": {"author": "Шевченко", "genre": "Поезія", "year": 1840, "pages": 200, "publish": "РМ"}
    }
    while True:
        print("Книжкова колекція:")
        print("1. Показати всю колекцію")
        print("2. Додати книгу")
        print("3. Видалити книгу")
        print("4. Пошук книги")
        print("5. Змінити книгу")
        print("0. Вихід")

        choice = input("Дія: ")
        if choice == "1":
            for title, d in library.items():
                print(f"'{title}' — {d['author']} ({d['year']} р.)")
        elif choice == "2":
            title = input("Введіть назву книги: ")
            if title in library:
                print("Книга вже є в колекції")
            else:
                try:
                    library[title] = {
                        "author": input("Введіть автора: "),
                        "genre": input("Введіть жанр: "),
                        "year": int(input("Введіть рік: ")),
                        "pages": int(input("вкажіть кількість сторінок: ")),
                        "publish": input("Ввдеіть видавництво: ")
                    }
                except ValueError:
                    print("Помилка: ви ввели некоректний формат")
        elif choice == "3":
            title = input("Введіть назву книги для видалення: ")
            if title in library:
                del library[title]
                print(f"Книгу {title} видалено")
            else:
                print("Книгу не знайдено")
        elif choice == "4":
            title = input("Введіть назву для пошуку: ")
            d = library.get(title)
            if d:
                for k, v in d.items(): print(f"{k}: {v}")
        elif choice == "5":
            title = input("Введіть назву книги для зміни: ")
            if title in library:
                try:
                    library[title]["author"] = input("Введіть нового автора")
                    library[title]["genre"] = input("Введіть новий жанр")
                    library[title]["year"] = int(input("Введіть нову рік написання"))
                    library[title]["pages"] = int(input("Введіть нову кількість сторінок"))
                    library[title]["publish"] = input("Введіть нове видавництво")
                    print("Успішно оновлено")
                except ValueError:
                    print("Помилка: ви ввели некоректний формат")
            else:
                print("Не знайдено")
        elif choice == "0":
            break
def main():
    #basketball_menu()
    #dictionary_menu()
    #firma_menu()
    books_menu()
if __name__ == "__main__":
    main()

