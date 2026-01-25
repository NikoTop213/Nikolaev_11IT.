number = 3
attempts = 3

for attempt in range(1, attempts + 1):
    guess = int(input("Введите загаданое число: "))

    if guess == number:
        print("Угадали!")
        break
    else:
        print("Неверно")
    if guess < number:
        print("Загаданное число больше")
    else:
            print("Загаданное число меньше")
    if attempt == attempts:
            print(f"Было загадано число {number}")