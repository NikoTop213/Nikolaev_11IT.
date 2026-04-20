labirint = input('Введите 25 символов в лабиринте: ')
print()

if len(labirint) != 25:
    print('Ошибка❌ Должно быть 25 символов!')
else:
    for i in range(0, 25, 5):
        ryad = labirint[i:i+5]
        print(f'{ryad}')

    n_index = labirint.find('н')
    f_index = labirint.find('ф')

    if n_index == -1:
        print('Ошибка❌ Вход в лабиринт не найден!')
    elif f_index == -1:
        print('Ошибка❌ Вход в лабиринт не найден!')
    else:
        row_n = n_index // 5
        stolb_n = n_index % 5

        row_f = f_index // 5
        stolb_f = f_index % 5

        manhetten_distance = abs(row_n - row_f) + abs(stolb_n - stolb_f)

        print()
        print(f'Вход в лабиринт находится в строке {row_n + 1} и столбце {stolb_n + 1}')
        print(f'Выход в лабиринт находится в строке {row_f + 1} и столбце {stolb_f + 1}')
        print(f'Манхэттенское расстояние между входом и выходом равно {manhetten_distance}')

        coin = labirint.count('м')

        if coin == 0:
            print('🪙х0')
        else:
            print(f'🪙x{coin}')

        lovushki = labirint.count('л')
        vragi = labirint.count('з')

        health = 100
        damage = lovushki * 10 + vragi * 50
        total_health = health - damage

        heart = total_health // 10
        heart_full = '♥' * heart

        lost_heart = damage // 10
        heart_null = '♡' * lost_heart

        total_hearts = heart_full + heart_null

        print(f'Оставшееся здоровье: {total_hearts}')