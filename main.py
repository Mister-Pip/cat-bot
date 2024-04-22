from some_API import TG_API
import telebot


bot = telebot.TeleBot(TG_API)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


bot.polling(none_stop=True)

