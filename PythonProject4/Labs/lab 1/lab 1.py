try:
    zavd = int(input("Введіть завдання (1-3): "))

    if zavd == 1:
        # Завдання 1
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        додавання = num1 + num2
        віднімання = num1 - num2
        множення = num1 * num2

        print(f"Результат додавання: {додавання}")
        print(f"Результат віднімання: {віднімання}")
        print(f"Результат множення: {множення}")

        if num2 != 0:
            ділення = num1 / num2
            print(f"Результат ділення: {ділення}")
        else:
            print("Неможливо ділити на 0.")

    elif zavd == 2:
        # Завдання 2
        def calculate_distance(V1, V2):
            t1 = 2 - (2 * 20 / 60)
            t2 = 2 - (10 / 60)
            distance1 = V1 * t1
            distance2 = V2 * t2
            total_distance = distance1 + distance2
            return total_distance

        V1 = float(input("Введіть швидкість першого автомобіля: "))
        V2 = float(input("Введіть швидкість другого автомобіля: "))

        distance = calculate_distance(V1, V2)
        print(f"Відстань між автомобілями через дві години: {distance:.2f} км")

    elif zavd == 3:
        # Завдання 3
        R = float(input("Введіть довжину маршруту R (км): "))
        R1 = float(input("Введіть довжину маршруту R1 (км): "))
        R1_m = 800 / 1000
        R2 = float(input("Введіть довжину маршруту R2 (км): "))
        R3 = float(input("Введіть довжину маршруту R3 (км): "))
        R3_m = float(input("Введіть довжину маршруту R3 (м): ")) / 1000
        K = int(input("Введіть кількість маршрутів довжиною R1 до K: "))

        if K > 5:
            d_R1 = K * (R1 + R1_m)
        else:
            print("Неможливо виконати обчислення, оскільки K <= 5.")


        d_R = 3 * R
        d_R3 = 8 - (3 + K)
        d_R3 = d_R3 * (R3 + R3_m)

        t = d_R + d_R1 + d_R3
        print(f"Загальна відстань, пройдена туристом: {t:.2f} км")

    else:
        print("Невірне завдання! Введіть число від 1 до 3.")

except ValueError:
    print("Помилка вводу. Будь ласка, введіть числові значення.")

