import telebot

TOKEN = "8784478472:AAEBbF55kNDVpDUNIGhp3X1D_wwAt4R_1Kc"
bot = telebot.TeleBot(TOKEN)

# Пример база отелей
hotels = [
    {"name": "Rixos Premium", "city": "Almaty", "price": 45000, "rating": 5},
    {"name": "Holiday Inn", "city": "Astana", "price": 30000, "rating": 4},
    {"name": "Novotel", "city": "Shymkent", "price": 25000, "rating": 4},
    {"name": "Renion Park", "city": "Almaty", "price": 18000, "rating": 3},
    {"name": "Hilton", "city": "Astana", "price": 60000, "rating": 5}
]

# Временное состояние пользователя
user_filters = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🏨 *Чат-бот поиска отелей*\n\n"
        "Напишите город, например: *Almaty*",
        parse_mode="Markdown"
    )
    user_filters[message.chat.id] = {"city": None, "min_price": None, "max_price": None, "rating": None}

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    chat_id = message.chat.id
    state = user_filters.get(chat_id)

    # Если город не выбран
    if state["city"] is None:
        state["city"] = message.text.strip()
        bot.send_message(chat_id, "Введите *минимальную цену* (тенге):", parse_mode="Markdown")
        return

    # Минимальная цена
    if state["min_price"] is None:
        if not message.text.isdigit():
            bot.send_message(chat_id, "Только число. Введите минимальную цену:")
            return
        state["min_price"] = int(message.text)
        bot.send_message(chat_id, "Введите *максимальную цену*:")
        return

    # Максимальная цена
    if state["max_price"] is None:
        if not message.text.isdigit():
            bot.send_message(chat_id, "Только число. Введите максимальную цену:")
            return
        state["max_price"] = int(message.text)
        bot.send_message(chat_id, "Введите *минимальный рейтинг* (1–5):")
        return

    # Рейтинг
    if state["rating"] is None:
        if not message.text.isdigit() or not (1 <= int(message.text) <= 5):
            bot.send_message(chat_id, "Введите рейтинг от 1 до 5:")
            return
        state["rating"] = int(message.text)

        # Готов искать
        show_results(message, state)
        user_filters[chat_id] = {"city": None, "min_price": None, "max_price": None, "rating": None}


def show_results(message, filters):
    city = filters["city"].lower()
    min_p = filters["min_price"]
    max_p = filters["max_price"]
    rating = filters["rating"]

    result = []

    for h in hotels:
        if (
            h["city"].lower() == city
            and min_p <= h["price"] <= max_p
            and h["rating"] >= rating
        ):
            result.append(h)

    if not result:
        bot.send_message(message.chat.id, "❌ Отели по вашему запросу не найдены.")
        return

    text = "🏨 *Найденные отели:*\n\n"
    for h in result:
        text += (
            f"• *{h['name']}*\n"
            f"  📍 Город: {h['city']}\n"
            f"  💵 Цена: {h['price']} ₸\n"
            f"  ⭐ Рейтинг: {h['rating']}/5\n\n"
        )

    bot.send_message(message.chat.id, text, parse_mode="Markdown")