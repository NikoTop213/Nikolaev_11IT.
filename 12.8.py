print('Обмен значений')
import random

A = [random.randint(1, 100) for i in range(5)]
print('Список чисел: ', A)
print()

min_A = A.index(min(A))
A[0], A[min_A] = A[min_A], A[0]
print('Измененная версия списка: ', A)