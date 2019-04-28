import random

def passwordGeneration(quantity):
    alphabetNumbers = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    random.shuffle(alphabetNumbers)

    return ''.join([random.choice(alphabetNumbers) for i in range(quantity)])


while True:
    if input("Сгенерировать пароль? (Да/Нет) : ").lower() == "да":
        print("Пароль готов: ", passwordGeneration(int(input("Введите количество символов для пароля: "))))
    else:
        break
