def calculate_fuel_needed(distance_km: float, fuel_consumption_per_100km: float):
    return distance_km * (fuel_consumption_per_100km / 100)
def calculate_trip_cost(fuel_needed_liters: float, price_per_liter: float):
    return fuel_needed_liters * price_per_liter
def main():
    print("Калькулятор стоимости поездки")

    distance = float(input("Введите расстояние поездки (км): "))
    consumption = float(input("Введите расход топлива (л на 100 км): "))
    price = float(input("Введите цену топлива за литр (руб): "))

    fuel_needed = calculate_fuel_needed(distance, consumption)
    trip_cost = calculate_trip_cost(fuel_needed, price)

    print("Результаты расчёта")
    print(f"Потребуется топлива: {fuel_needed:.2f} л")
    print(f"Стоимость поездки: {trip_cost:.2f} руб")
if __name__ == "__main__":
    main()