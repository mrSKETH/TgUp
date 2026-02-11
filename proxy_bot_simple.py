import telebot
from telebot import types

# Токен бота (получите у @BotFather)
TOKEN = "8188317423:AAErG71gKMEf-EdLSjFXwjCvFblCOguLKpM"

bot = telebot.TeleBot(TOKEN)

# Список прокси
PROXIES = {
    "proxy1": {
        "name": "🌐 General",
        "url": "https://t.me/proxy?server=185.130.115.1>
        "desc": "Основной сервер"
    },
    "proxy2": {
        "name": "⚡ Alt 1",
        "url": "https://t.me/proxy?server=146.185.208.1>
        "desc": "1 Запасной"
    },
    "proxy3": {
        "name": "🇪🇺 Fast",
        "url": "https://t.me/proxy?server=www.download->
        "desc": "С минимальным пингом"
    }
}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    for proxy_id, proxy_data in PROXIES.items():
        btn = types.InlineKeyboardButton(
            text=proxy_data["name"],
            callback_data=f"proxy_{proxy_id}"
        )
        markup.add(btn)

    bot.send_message(
        message.chat.id,
        "🤖 **Бот для ускорения телеграмм**\n\nВыберите>
        reply_markup=markup,
        parse_mode="Markdown"
    )

# Обработка нажатий кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data.startswith("proxy_"):
        proxy_id = call.data.replace("proxy_", "")

        if proxy_id in PROXIES:
            proxy = PROXIES[proxy_id]

            markup = types.InlineKeyboardMarkup()
            btn_connect = types.InlineKeyboardButton(
                text="🔗 Подключиться",
                url=proxy["url"]
            )
            btn_back = types.InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back"
            )
            markup.add(btn_connect, btn_back)

            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=f"**{proxy['name']}**\n\n"
                     f"📝 *Описание:* {proxy['desc']}\n>
                reply_markup=markup,
                parse_mode="Markdown"
            )

    elif call.data == "back":
        markup = types.InlineKeyboardMarkup(row_width=1)

        for proxy_id, proxy_data in PROXIES.items():
            btn = types.InlineKeyboardButton(
                text=proxy_data["name"],
                callback_data=f"proxy_{proxy_id}"
            )
            markup.add(btn)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🤖 **Бот для подключения прокси Teleg>
            reply_markup=markup,
            parse_mode="Markdown"
        )

    bot.answer_callback_query(call.id)
# Команда /help
@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(
        message.chat.id,
        "📋 **Доступные команды:**\n"
        "/start - начать работу\n"
        "/help - помощь\n\n"
        "Просто нажмите /start и выберите прокси!"
    )

print("🤖 Бот запустился!")
bot.polling(none_stop=True)
