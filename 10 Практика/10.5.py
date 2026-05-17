print('Меню операций банкомата')

balance = 1000

while True:
    print('Меню')
    print('1. Узнать баланс')
    print('2. Снять 100 руб')
    print('3. Положить 100 руб')
    print('4. Выход')
    print()

    сomand = int(input('Выберите номер команды: '))

    if сomand == 1:
        print(f'Ваш баланс {balance} руб')
    elif сomand == 2:
        if balance >= 100:
            balance -= 100
            print('Снято 100 руб')
        else:
            print('Недостаточно средств')
    elif сomand == 3:
        balance += 100
        print('Зачислено 100 руб')
    elif сomand== 4:
        print('покеда')
        break
    else:
        print('Ошибка')
