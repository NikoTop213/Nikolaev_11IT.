temperature = float(input("Введите температуру: "))
pressure = int(input("Введите давление: "))
pulse = int(input("Введите пульс: "))

if temperature < 35 or temperature > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110:
    print("Состояние требует врача")
elif 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("Cостояние в норме")
elif (35 <= temperature < 36 or 37 < temperature <= 38) or (105 <= pressure <= 110 or 130 < pulse <= 140) or (55 <= pulse <= 60 or 100 <= pulse <= 110):
    print("Лёгкое недомогание")
else:
    print("Состояние не получается определить")