import numpy as np
import matplotlib.pyplot as plt
import collections
import re

try:
    zavd = int(input("Введіть завдання (1-3): "))

    if zavd == 1:
        # Завдання 1
        x = np.linspace(0.1, 4, 400)
        y = np.sin(10 * x) * np.sin(3 * x) / (x ** 2)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='Y(x)=sin(10*x)*sin(3*x)/(x^2)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Графік функції Y(x)=sin(10*x)*sin(3*x)/(x^2)')
        plt.legend()
        plt.grid()
        plt.show()

    elif zavd == 2:
        # Завдання 2
        text = """
        Привіт.Як справи?Го в діскорд?
        """

        text_cleaned = re.sub(r'[^а-яА-Яa-zA-Z]', '', text)
        letter_counts = collections.Counter(text_cleaned.lower())

        plt.figure(figsize=(10, 6))
        plt.bar(letter_counts.keys(), letter_counts.values(), color='skyblue')
        plt.xlabel('Літера')
        plt.ylabel('Частота')
        plt.title('Частота появи літер у тексті')
        plt.grid(axis='y')
        plt.show()

    elif zavd == 3:
        # Завдання 3
        text_sentences = """
        Я йду в коледж.Го в Дс?Погнала в кіно!Це просто...Окей.
        """

        regular_sentences = len(re.findall(r'[^!?\\.]{1,}\\.', text_sentences))
        question_sentences = len(re.findall(r'\\?', text_sentences))
        exclamation_sentences = len(re.findall(r'!', text_sentences))
        ellipsis_sentences = len(re.findall(r'\\.\\.\\.', text_sentences))

        sentence_types = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапка']
        sentence_counts = [regular_sentences, question_sentences, exclamation_sentences, ellipsis_sentences]

        plt.figure(figsize=(10, 6))
        plt.bar(sentence_types, sentence_counts, color='lightgreen')
        plt.xlabel('Тип речення')
        plt.ylabel('Кількість')
        plt.title('Частота появи різних типів речень у тексті')
        plt.grid(axis='y')
        plt.show()

    else:
        print("Невірне завдання! Введіть число від 1 до 3.")

except ValueError:
    print("Будь ласка, введіть ціле число.")
