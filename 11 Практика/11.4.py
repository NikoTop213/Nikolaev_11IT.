num = input("Введите число: ")

count_3 = 0
last_digit = 0
count_last = 0
count_even = 0
sum_bolshe_5 = 0
proiz_bolshe_7 = 0
found_7 = False
count_0_5 = 0

for ch in num:
    digit = int(ch)

    if digit == 3:
        count_3 += 1
    if ch == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_bolshe_5 += digit
    if digit > 7:
        proiz_bolshe_7 += digit
        found_7 = True
    if digit == 0 or digit == 5:
        count_0_5 += 1

if not found_7:
    proiz_bolshe_7 = 1

print(count_3)
print(count_last)
print(count_even)
print(sum_bolshe_5)
print(proiz_bolshe_7)
print(count_0_5)