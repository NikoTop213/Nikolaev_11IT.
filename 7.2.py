print("\n"+ "="*30)
print("\n 📦 СТАТУС ВАШЕГО ЗАКАЗА 📦")
print("\n"+ "="*30)
status = input("Введите статус заказа (pending/processing/shipped/delivered/cancelled): ")

match status:
    case "pending":
        text = "⏳ В ожидании ⏳"
        desc = "Заказ зарегистрирован и ожидает подтверждения."
        time = "Обычно 1–2 дня"
    case "processing":
        text = "⚙️ В обработке ⚙️"
        desc = "Заказ собирается и подготавливается к отправке."
        time = "Обычно 2–3 дня"
    case "shipped":
        text = "✈️ Отправлено ✈️"
        desc = "Заказ передан службе доставки и находится в пути."
        time = "Обычно 2–5 дней"
    case "delivered":
        text = "📬 Доставлено 📬"
        desc = "Заказ прибыл и успешно вручён получателю."
        time = "Доставка завершена"
    case "cancelled":
        text = "❌ Отменено ❌"
        desc = "Заказ был отменён покупателем или магазином."
        time = "Нет ожидания – заказ закрыт"
    case _:
        print("⚠️ Неизвестный статус 'invalid_status' ")

print(f"Статус: {text} ")
print(f"Описание: {desc}")
print(f"Примерное время обработки: {time}")