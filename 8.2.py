result ='YES'
for i in range(10):
    n = int(input('Введите 10 чисел (через enter): '))
    if n % 2 != 0:
        result = 'NO'

print(result)