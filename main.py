from pycbrf import ExchangeRates
# pycbrf берёт БД из офиального сайта Центрального банка по котировке
from datetime import datetime
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    # Создание банальных кнопок
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               row_width=2)
    item_1 = telebot.types.KeyboardButton('USD')
    item_2 = telebot.types.KeyboardButton('EUR')
    item_3 = telebot.types.KeyboardButton('CNY')  # Китайский юань
    markup.add(item_1, item_2, item_3)
    bot.send_message(chat_id=message.chat.id,
                     text='<b>Hello, Choose pls your value,</b>',
                     reply_markup=markup,
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def message(message):
    NOV = message.text.strip().lower()
    # NOV = name of value
    if NOV in ['usd', 'eur', 'cny']:
        rates = ExchangeRates(datetime.now())
        main = NOV.upper()  # Example: usd=USD, eur=EUR
        value = float(rates[NOV.upper()].rate)  # numbers
        bot.send_message(chat_id=message.chat.id,
                         text=f'{main} курс сейчас {value}')


bot.polling(none_stop=True)
