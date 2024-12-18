import os
import sys
import importlib.util

LABS_DIR = "labs"

def run_lab(lab_number):
    try:
        labs = [lab for lab in os.listdir(LABS_DIR) if os.path.isdir(os.path.join(LABS_DIR, lab))]
        labs.sort()

        if lab_number < 1 or lab_number > len(labs):
            print("Невірний номер лабораторної роботи.")
            return

        selected_lab = labs[lab_number - 1]
        lab_script_path = os.path.join(LABS_DIR, selected_lab, f"{selected_lab}.py")

        if not os.path.exists(lab_script_path):
            print(f"Файл {lab_script_path} не знайдено.")
            return

        print(f"Запуск лабораторної роботи {lab_number} ({selected_lab})...")
        spec = importlib.util.spec_from_file_location(selected_lab, lab_script_path)
        lab_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lab_module)

    except Exception as e:
        print(f"Сталася помилка під час виконання лабораторної роботи: {e}")
def list_labs():

    if not os.path.exists(LABS_DIR):
        print("Папка з лабораторними роботами не знайдена.")
        return

    labs = [lab for lab in os.listdir(LABS_DIR) if os.path.isdir(os.path.join(LABS_DIR, lab))]
    if not labs:
        print("Немає доступних лабораторних робіт.")
        return

    print("Доступні лабораторні роботи:")
    for i, lab in enumerate(labs, start=1):
        readme_path = os.path.join(LABS_DIR, lab, "README.md")
        description = "Немає опису"
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                description = f.readline().strip()
        print(f"{i}. {lab} - {description}")



def print_help():
    print("Команди CLI:")
    print("list")
    print("run <lab_number>")
    print("help")


def main():

    if len(sys.argv) < 2:
        print("Помилка! Використовуйте 'help' для списку команд.")
        return

    command = sys.argv[1].lower()

    if command == "list":
        list_labs()
    elif command == "run":
        if len(sys.argv) != 3:
            print("Вкажіть номер лабораторної роботи. Приклад: 'run 1'")
            return
        try:
            lab_number = int(sys.argv[2])
            run_lab(lab_number)
        except ValueError:
            print("Номер лабораторної роботи повинен бути числом!")
    elif command == "help":
        print_help()
    else:
        print(f"Невідома команда: {command}. Використовуйте 'help' для списку команд.")


if __name__ == "__main__":
    main()