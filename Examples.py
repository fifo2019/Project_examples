from random import randint

def calcul():
    correct_answer = 0
    wrong_answers = 0
    counter = 0
    while True:
        if counter < 100:
            counter += 1
            print("Умножайка!")
            a = randint(1, 7)
            b = randint(1, 7)
            print(a, "*", b, " =", "?")
            try:
                user = int(input())
                if user == a * b:
                    correct_answer += 1
                    print("Это правильный ответ! Вы молодец!")
                else:
                    print("Вы не правильно ответили! Учи таблицу!")
                    wrong_answers += 1
            except ValueError:
                print("Пожалуйста, введите число!")
        else:
            break
    print("Прощай!", "\nРешено примеров ", counter, "\nПравильных решений ", correct_answer, "\nРешено не верно ", wrong_answers)

calcul()

print("Чтобы выйти, жми Enter")