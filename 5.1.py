print("Калькулятор налогов")
TAX_RATE= 0.13
income = float(input("ВВедите ваш годовой доход: "))


tax= income * TAX_RATE
Sum_hands = income - tax
print(f"общая сумма дохода: {income:,.2f} руб.")
print(f'Сумма расчитанного налога: {tax:,.2f} руб.')
print(f'сумма на руку после налога:{Sum_hands:,.2f} руб.')
