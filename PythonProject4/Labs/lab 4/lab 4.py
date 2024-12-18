import random

def zavd1():
    names = ["Іван", "Марія", "Петро", "Ольга", "Сергій", "Анастасія"]
    verbs = ["малює", "читає", "пише", "співає", "гуляє", "вивчає"]
    objects = ["картину", "книгу", "вірш", "пісню", "твір", "фото"]

    def generate_phrase():
        first_word = random.choice(names)
        second_word = random.choice(verbs)
        third_word = random.choice(objects)
        return f"{first_word} {second_word} {third_word}"

    random_phrase = generate_phrase()
    print("Згенерована фраза:", random_phrase)

def zavd2():
    file_path = "book.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            with_spaces = len(text)
            without_spaces = len(text.replace(" ", ""))
            print(f"Кількість символів з пробілами: {with_spaces}")
            print(f"Кількість символів без пробілів: {without_spaces}")
    except FileNotFoundError as e:
        print(f"Помилка: файл не знайдено. {e.filename}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def zavd3():
    def sentence_analysis(text):
        sentences = text.split('. ') + text.split('! ') + text.split('? ') + text.split('… ')
        total_sentences = len(sentences)
        exclamatory_sentences = text.count('!')
        question_sentences = text.count('?')
        ellipsis_sentences = text.count('…')
        print("Загальна кількість речень:", total_sentences)
        print("Кількість окличних речень:", exclamatory_sentences)
        print("Кількість питальних речень:", question_sentences)
        print("Кількість речень з трикрапкою:", ellipsis_sentences)

    text = "Привіт! Як справи? Го в дс?Скоро буду....."
    sentence_analysis(text)

def main():
    try:
        zavdana = int(input("Номер завдання (1-3): "))

        if zavdana == 1:
            zavd1()
        elif zavdana == 2:
            zavd2()
        elif zavdana == 3:
            zavd3()
        else:
            print("Введіть число лише від 1 до 3.")
    except ValueError:
        print("Ведіть  від 1 до 3!!.")

if __name__ == "__main__":
    main()

