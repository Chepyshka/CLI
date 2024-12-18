# -*- coding: utf-8 -*-


class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' автор {self.author} ({self.year}) - Жанр: {self.genre}"


class HomeLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{title}' видалена з бібліотеки.")
                return
        print(f"Книга '{title}' не знайдена у бібліотеці.")

    def find_books_by_author(self, author):
        results = [book for book in self.books if book.author.lower() == author.lower()]
        return results

    def find_books_by_year(self, year):
        results = [book for book in self.books if book.year == year]
        return results

    def find_books_by_genre(self, genre):
        results = [book for book in self.books if book.genre.lower() == genre.lower()]
        return results

    def get_book_by_index(self, index):
        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            print("Неправильний індекс.")
            return None

    def display_books(self):
        if not self.books:
            print("Бібліотека порожня.")
        else:
            print("Книги у бібліотеці:")
            for idx, book in enumerate(self.books):
                print(f"{idx + 1}. {book}")


# Демонстрація роботи з класом HomeLibrary
library = HomeLibrary()

print("Вітаємо у домашній бібліотеці!")

while True:
    print("\nМеню:")
    print("1. Додати книгу")
    print("2. Відобразити всі книги")
    print("3. Знайти книги за автором")
    print("4. Знайти книги за роком видання")
    print("5. Знайти книги за жанром")
    print("6. Отримати книгу за індексом")
    print("7. Видалити книгу")
    print("8. Вийти")

    choice = input("Оберіть опцію (1-8): ")

    if choice == "1":
        book_info = input("Введіть книгу у форматі 'Назва, Автор, Рік, Жанр': ")
        try:
            title, author, year, genre = map(str.strip, book_info.split(","))
            library.add_book(Book(title, author, int(year), genre))
        except ValueError:
            print("Помилка вводу. Перевірте формат (Назва, Автор, Рік, Жанр).")

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        author_search = input("Введіть ім'я автора для пошуку: ")
        print(f"\nКниги автора {author_search}:")
        for book in library.find_books_by_author(author_search):
            print(book)

    elif choice == "4":
        try:
            year_search = int(input("Введіть рік видання для пошуку: "))
            print(f"\nКниги, видані у {year_search} році:")
            for book in library.find_books_by_year(year_search):
                print(book)
        except ValueError:
            print("Помилка вводу. Введіть числове значення для року.")

    elif choice == "5":
        genre_search = input("Введіть жанр для пошуку: ")
        print(f"\nКниги у жанрі '{genre_search}':")
        for book in library.find_books_by_genre(genre_search):
            print(book)

    elif choice == "6":
        try:
            index = int(input("Введіть індекс книги для отримання інформації: ")) - 1
            book = library.get_book_by_index(index)
            if book:
                print(f"\nКнига за індексом {index + 1}: {book}")
        except ValueError:
            print("Помилка вводу. Введіть числове значення для індексу.")

    elif choice == "7":
        title_to_remove = input("Введіть назву книги для видалення: ")
        library.remove_book(title_to_remove)

    elif choice == "8":
        print("До побачення!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
