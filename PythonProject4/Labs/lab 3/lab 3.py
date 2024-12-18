import os

def write_to_file(group_name, student_name, average_grade):
    try:
        file_name = f"{group_name}.txt"
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"{student_name},{average_grade}\n")
        print(f"Дані записано до файлу {file_name}.")
    except Exception as e:
        print(f"Помилка запису в файл: {e}")


def read_file(group_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                print(file.read())
        except Exception as e:
            print(f"Помилка читання файлу: {e}")
    else:
        print(f"Файл {file_name} не існує.")


def search_in_file(group_name, student_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                found = False
                for line in file:
                    name, grade = line.strip().split(',')
                    if name == student_name:
                        print(f"Знайдено: {name} - {grade}")
                        found = True
                if not found:
                    print(f"Студента {student_name} не знайдено в файлі {file_name}.")
        except Exception as e:
            print(f"Помилка при пошуку в файлі: {e}")
    else:
        print(f"Файл {file_name} не існує.")


def sort_file_by_grade(group_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                students = [line.strip().split(',') for line in file]
            students.sort(key=lambda x: float(x[1]), reverse=True)
            with open(file_name, 'w', encoding='utf-8') as file:
                for name, grade in students:
                    file.write(f"{name},{grade}\n")
            print(f"Файл {file_name} відсортовано за середнім балом.")
        except Exception as e:
            print(f"Помилка при сортуванні файлу: {e}")
    else:
        print(f"Файл {file_name} не існує.")


def list_files():
    try:
        files = [f for f in os.listdir() if f.endswith('.txt')]
        if files:
            print("Знайдені файли:")
            for file in files:
                print(file)
        else:
            print("Файлів не знайдено.")
    except Exception as e:
        print(f"Помилка при отриманні списку файлів: {e}")


def main():
    while True:
        print("\nМеню:")
        print("1. Додати студента")
        print("2. Переглянути дані групи")
        print("3. Знайти студента в групі")
        print("4. Відсортувати дані групи за середнім балом")
        print("5. Показати всі файли")
        print("6. Вийти")

        choice = input("Виберіть що Вам потрібно: ")

        if choice == '1':
            group = input("Введіть назву групи: ")
            name = input("Введіть ім'я студента: ")
            try:
                grade = float(input("Введіть середній бал:"))
                write_to_file(group, name, grade)
            except ValueError:
                print("Помилка вводу.")
        elif choice == '2':
            group = input("Введіть назву групи: ")
            read_file(group)
        elif choice == '3':
            group = input("Введіть назву групи: ")
            name = input("Введіть ім'я студента: ")
            search_in_file(group, name)
        elif choice == '4':
            group = input("Введіть назву групи: ")
            sort_file_by_grade(group)
        elif choice == '5':
            list_files()
        elif choice == '6':
            print("Завершено.")
            break
        else:
            print("Помилка!")


if __name__ == "__main__":
    main()

