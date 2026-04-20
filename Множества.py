# Уровень 1

text = input('Введите слова: ').split()

count = len(set(text))
slova = sorted(set(text))
spisok = " ".join(slova)

print(f'Количество: {count}')
print(f'Слова: {spisok}')

# Уровень 2

id_ok = input('Введите разрешенные айди')
Id_ok = set(id_ok)

vhod_id = input('Введите айди: ').split()

for i in vhod_id:
    if i in Id_ok:
        print('OK')
    else:
        print('ADDED')
        Id_ok.add(i)

# Уровень 3

A = set(input('Введите имена файлов: ').split())
B = set(input('Введите имена файлов: ').split())

common = sorted(A & B)
lost = sorted(A - B)
print(f'Общие имена {common}')
print(f'Потерянные имена {lost}')

# Уровень 4

CRU = set(input('Введите имена: ').split())
MI_6 = set(input('Введите имена: ').split())
KGB = set(input('Введите имена: ').split())

agents = sorted((CRU & MI_6) - KGB, reverse=True)
print(agents)

# Уровень 5

ip_1 = set(input('Введите айпи адрес: ').split())
ip_2 = set(input('Введите айпи адрес: ').split())
ip_3 = set(input('Введите айпи адрес: ').split())

result = sorted((ip_1 | ip_2 | ip_3) - (ip_1 & ip_2 & ip_3))
print(result)

# Уровень 6

id_1 = set(map(int, input('Введите айди: ').split()))
id_2 = set(map(int, input('Введите айди: ').split()))
id_3 = set(map(int, input('Введите айди: ').split()))

all_ids = set(range(11))
prizraki = (all_ids - (id_1 | id_2 | id_3))
print(prizraki)

# Уровень 7

agent = (2,2)
save_point = [(1,1), (5,5), (0,3)]
nearest = save_point[0]
for i in save_point:
    distance = abs(i[0] - 2) + abs(i[1] - 2)
    if distance < abs(nearest[0] - 2) + abs(nearest[1] - 2):
        nearest = i
print(nearest)