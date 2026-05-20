import telebot
from telebot import types

TOKEN = "8910874633:AAEz4OHG9ASLWYOYyFhBOheqc0dkUELQKtU"

bot = telebot.TeleBot(TOKEN)

# START MENU
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🏠 Комнаты")
    btn2 = types.KeyboardButton("💰 Цены")
    btn3 = types.KeyboardButton("📍 Адрес")
    btn4 = types.KeyboardButton("📞 Контакты")
    btn5 = types.KeyboardButton("ℹ️ О нас")

    btn6 = types.KeyboardButton("🛏 Бронирование")
    btn7 = types.KeyboardButton("📷 Фото")
    btn8 = types.KeyboardButton("📶 WiFi")
    btn9 = types.KeyboardButton("🍽 Питание")
    btn10 = types.KeyboardButton("📜 Правила")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    markup.add(btn6, btn7)
    markup.add(btn8, btn9, btn10)

    bot.send_message(
        message.chat.id,
        "🏨 Добро пожаловать в Hostel Bot!\nВыберите раздел:",
        reply_markup=markup
    )

# BUTTON HANDLER
@bot.message_handler(func=lambda message: True)
def message_reply(message):

    text = message.text

    if text == "🏠 Комнаты":
        bot.send_message(
            message.chat.id,
            "🛏 Комнаты:\n\n"
            "• 1-местная\n"
            "• 2-местная\n"
            "• Общая комната"
        )

    elif text == "💰 Цены":
        bot.send_message(
            message.chat.id,
            "💰 Цены:\n\n"
            "• 1-местная — 8000 тг\n"
            "• 2-местная — 5000 тг\n"
            "• Общая — 3000 тг"
        )

    elif text == "📍 Адрес":
        bot.send_message(
            message.chat.id,
            "📍 Алматы, Абая 150"
        )

    elif text == "📞 Контакты":
        bot.send_message(
            message.chat.id,
            "📞 Телефон: +7 702 742 70 47\n"
            "📩 Telegram: @hostel_admin"
        )

    elif text == "ℹ️ О нас":
        bot.send_message(
            message.chat.id,
            "🏨 Уютный hostel для студентов и туристов."
        )

    elif text == "🛏 Бронирование":
        bot.send_message(
            message.chat.id,
            "📅 Напишите дату и тип комнаты.\n"
            "Пример: 25 мая, 2-местная"
        )

    elif text == "📷 Фото":
        bot.send_message(
            message.chat.id,
            "📸 Фото скоро будут добавлены!"
        )

    elif text == "📶 WiFi":
        bot.send_message(
            message.chat.id,
            "📶 WiFi\n"
            "Сеть: Hostel_Free\n"
            "Пароль: 12345678"
        )

    elif text == "🍽 Питание":
        bot.send_message(
            message.chat.id,
            "🍽 Завтрак включён.\n"
            "Обед и ужин по заказу."
        )

    elif text == "📜 Правила":
        bot.send_message(
            message.chat.id,
            "📜 Правила:\n"
            "• Тишина после 23:00\n"
            "• Курение запрещено\n"
            "• Соблюдать чистоту"
        )

    else:
        bot.send_message(
            message.chat.id,
            "👇 Выберите кнопку из меню"
        )

print("Hostel Bot запущен...")
bot.infinity_polling()