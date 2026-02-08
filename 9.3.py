coin = int(input("Введите сумму: "))
count = 0

while coin >= 25:
    count += 1
    coin -= 25

while coin >= 10:
    count += 1
    coin -= 10

while coin >= 5:
    count += 1
    coin -= 5

while coin >= 1:
    count += 1
    coin -= 1

print(f"Количество монет для оплаты: {count}")