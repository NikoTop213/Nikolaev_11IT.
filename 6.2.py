print("Каз")
pocket = int(input("Введите номер кармана(0-36): "))

if pocket < 0 or pocket > 36:
    print("Ошибка")
elif pocket ==0:
    print("Зелёный")
elif 1<= pocket <= 10:
    if pocket % 2 == 0:
        print("Чёрный")
    else:
        print("Красный")
elif 11 <= pocket <= 18:
    if pocket % 2 == 0:
        print("Красный")
    else:
        print("Чёрный")
elif 19 <= pocket <= 28:
    if pocket % 2 == 0:
        print("Чёрный")
    else:
        print("Красный")
else: # 29-36
    if pocket % 2 == 0:
        print("Красный")
    else:
        print("Чёрный")

