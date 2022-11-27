import telebot
import random
from telebot import types

API_TOKEN = 'ВАШ ТОКЕН'
bot = telebot.TeleBot(API_TOKEN)
part = {}


game_start = False


matrix = [" ", " ", " ",
          " ", " ", " ",
          " ", " ", " "]


player = "0"
iscin = "X"

correct_symbol = False
incorrect_character = False


def new_matrix():
    global matrix
    matrix = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]


def first_def(first_cell, second_cell, third_cell):
    if first_cell == player and second_cell == player and third_cell == player:
        global correct_symbol
        correct_symbol = True


def second_def(first_cell, second_cell, third_cell):
    if first_cell == iscin and second_cell == iscin and third_cell == iscin:
        global incorrect_character
        incorrect_character = True


def third_def(first_cell, second_cell):
    if first_cell == player and second_cell == player:
        global posDef
        posDef = iscin


@bot.message_handler(commands=['start'])
def begin(message):
    layout = types.ReplyKeyboardMarkup(resize_keyboard=True)
    part[0] = types.KeyboardButton("Готов")
    layout.add(part[0])

    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Привет, {0.first_name}! Готов проиграть?)".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=layout)


@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == "Готов":
            global game_start
            game_start = True
        else:
            bot.send_message(message.chat.id, "Кажется, возникла ошибка!")

    if game_start == True:

        part = {}

        global layout
        layout = types.InlineKeyboardMarkup(row_width=9)

        i = 0

        for i in range(9):
            part[i] = types.InlineKeyboardButton(
                matrix[i], callback_data=str(i))

        layout.row(part[0], part[1], part[2])
        layout.row(part[3], part[4], part[5])
        layout.row(part[6], part[7], part[8])
        bot.send_message(message.chat.id, "Выбери клетку", reply_markup=layout)


@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):

        random_select = random.randint(0, 8)
        if matrix[random_select] == player:
            random_select = random.randint(0, 8)
        elif matrix[random_select] == iscin:
            random_select = random.randint(0, 8)
        if matrix[random_select] == " ":
            matrix[random_select] = iscin

    for i in range(9):
        if call.data == str(i):
            if (matrix[i] == " "):
                matrix[i] = player

        first_def(matrix[0], matrix[1], matrix[2])
        first_def(matrix[3], matrix[4], matrix[5])
        first_def(matrix[6], matrix[7], matrix[8])
        first_def(matrix[0], matrix[3], matrix[6])
        first_def(matrix[1], matrix[4], matrix[7])
        first_def(matrix[2], matrix[5], matrix[8])
        first_def(matrix[0], matrix[4], matrix[8])
        first_def(matrix[2], matrix[4], matrix[6])
        second_def(matrix[0], matrix[1], matrix[2])
        second_def(matrix[3], matrix[4], matrix[5])
        second_def(matrix[6], matrix[7], matrix[8])
        second_def(matrix[0], matrix[3], matrix[6])
        second_def(matrix[1], matrix[4], matrix[7])
        second_def(matrix[2], matrix[5], matrix[8])
        second_def(matrix[0], matrix[4], matrix[8])
        second_def(matrix[2], matrix[4], matrix[6])

        part[i] = types.InlineKeyboardButton(
            matrix[i], callback_data=str(i))

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Готов",
                          reply_markup=None)
    global layout
    layout.row(part[0], part[1], part[2])
    layout.row(part[3], part[4], part[5])
    layout.row(part[6], part[7], part[8])

    bot.send_message(call.message.chat.id,
                     "Выбери клетку", reply_markup=layout)
    global correct_symbol
    if correct_symbol:
        bot.send_message(call.message.chat.id, "Я проиграл!")
        new_matrix()

        correct_symbol = False
        game_start = False

    global incorrect_character
    if incorrect_character:
        bot.send_message(call.message.chat.id, "Я выиграл!")
        new_matrix()

        incorrect_character = False
        game_start = False


bot.polling()