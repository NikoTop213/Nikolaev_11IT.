print('калькулятор имт')
weight, height = map(float, input('введите вес в кг и рост в метрах:').split())
IMT= weight/(height*height)
print(IMT)