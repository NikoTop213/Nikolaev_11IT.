print("Определение сезона")
month = int(input("Введите число(1-12): "))

match month:
    case 12 | 1 | 2:
        print(f"Месяц №{month};Зима❄️")
    case 3 | 4 | 5:
        print(f"Месяц №{month};Весна🌸")
    case 6 | 7 | 8:
        print(f"Месяц №{month};Лето🏖️")
    case 9 | 10 | 11:
        print(f"Месяц №{month};Осень🍂")
    case _:
        print("ты ваще дурной?⁉️⁉️")