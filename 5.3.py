
JPY_TO_RUB = 0.5219
def convert_jpy_to_rub(amount):
    return amount * JPY_TO_RUB
jpy = float(input('Сумма в иенах:'))
rub= convert_jpy_to_rub(jpy)
print(f'{jpy:.2f}JPY={rub:.2f}RUB'.replace(',',' '))

