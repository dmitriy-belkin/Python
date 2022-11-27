import telebot
import random
from telebot import types
import sqlite3
from datetime import datetime as dt

API_TOKEN = 'ВАШ_ТОКЕН'
bot = telebot.TeleBot(API_TOKEN)

value = ''
oldvalue = ''

keyboard = telebot.types.InlineKeyboardMarkup()
[(keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
               telebot.types.InlineKeyboardButton('C', callback_data='C'),
               telebot.types.InlineKeyboardButton('<=', callback_data='<='),
               telebot.types.InlineKeyboardButton('/', callback_data='/')),

  keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
               telebot.types.InlineKeyboardButton('8', callback_data='8'),
               telebot.types.InlineKeyboardButton('9', callback_data='9'),
               telebot.types.InlineKeyboardButton('*', callback_data='*')),

  keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
               telebot.types.InlineKeyboardButton('5', callback_data='5'),
               telebot.types.InlineKeyboardButton('6', callback_data='6'),
               telebot.types.InlineKeyboardButton('-', callback_data='-')),

  keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
               telebot.types.InlineKeyboardButton('2', callback_data='2'),
               telebot.types.InlineKeyboardButton('3', callback_data='3'),
               telebot.types.InlineKeyboardButton('+', callback_data='+')),

  keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
               telebot.types.InlineKeyboardButton('0', callback_data='0'),
               telebot.types.InlineKeyboardButton(',', callback_data=','),
               telebot.types.InlineKeyboardButton('=', callback_data='=')))]


@bot.message_handler(commands=['start', 'calculater'])
def get_message(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, oldvalue
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value == 'Ошибка!'
    else:
        value += data

    if (value != oldvalue and value != '') or ('0' != oldvalue and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text='0', reply_markup=keyboard)
            oldvalue = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text=value, reply_markup=keyboard)
            oldvalue = value

    oldvalue = value
    if value == 'Ошибка!':
        value = ''

    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(' '.join(data))


bot.polling(none_stop=False, interval=0)

time = dt.now().strftime('%D %H:%M')
with open('log.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{value} - действие произошло {time}\n")

with sqlite3.connect("database.db") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        resalt INTEGER
    )""")

    cursor.execute("INSERT INTO users VALUES(?)", (value,))

    cursor.execute("SELECT * FROM users")

    print(cursor.fetchone())