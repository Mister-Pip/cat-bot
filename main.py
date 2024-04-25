import rand_fact, telebot, rand_img
from APIs import BOT_TOKEN
from telebot import types


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['start'])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    get_fact_btn = types.KeyboardButton('Get some facts.')
    get_pic_btn = types.KeyboardButton('Get some pics.')
    markup.row(get_fact_btn, get_pic_btn)
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Get some facts.':
        fact = rand_fact.get_fact()
        bot.send_message(message.chat.id, f"Here's your random fact:\n{fact}")
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Get some pics.':
        pic = rand_img.get_pic()
        bot.send_photo(message.chat.id, pic)
        bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)

