# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ ПРОТИВ ЧЕЛОВЕКА

import random
from random import randint
from random import choice


def acquaintance():
    global player_one, player_two, player_three
    player_three = 'Крупье'
    player_two = 'Искин'
    player_one = input(f'[{player_three}]: Назовите ваше имя: ')
    print(f'[{player_three}]: {player_one}, в сегодняшней игре вашим соперником будет {player_two}')
    return [player_one, player_two, player_three]


def quantity_and_random(players):
    global maximum_stroke, number_of_candies
    number_of_candies = int(2021)
    maximum_stroke = int(28)
    the_first_move = randint(0, 2)
    if the_first_move != 1:
        the_first_move = 0
    return [number_of_candies, maximum_stroke, int(the_first_move)]


bot_responses = ['берите, не стесняйтесь...', 'ваша очередь',
                 'что же вы медлите?', 'не тяните резину...', 'ну же?..',
                 'отсчитайте свою порцию конфет',
                 'любите сладенькое? Тогда смелее...',
                 'ходите же, черт возьми!']


def the_game_itself(candies, players, bot_responses):
    cnt = candies[2]
    sum = 0
    while candies[0] > 0:
        if candies[0] == (maximum_stroke and candies[0] > 1):
            motion = candies[0] - 1
            if motion == 1 or motion == 21:
                print(f'[{player_two}]: Я беру {motion} конфету')
            elif 2 <= motion < 5:
                print(f'[{player_two}]: Мои {motion} конфеты')
            else:
                print(f'[{player_two}]: Извините, забираю {motion} конфет')
        elif not cnt % 2:
            motion = random.randint(1, candies[1])
            if motion == 1 or motion == 21:
                print(f'[{player_two}]: Я беру {motion} конфету')
            elif 2 <= motion < 5:
                print(f'[{player_two}]: Мои {motion} конфеты')
            else:
                print(f'[{player_two}]: Извините, забираю {motion} конфет')
        else:
            print(f'[{player_two}]: {players[0]}, {choice(bot_responses)}')
            motion = int(input())
            if motion > candies[1]:
                print(f'[{player_three}]: Можно взять не более {candies[1]} конфет')
                mistake = 2
                while mistake >= 0:
                    if candies[0] >= motion <= candies[1]:
                        break
                    print(
                        f'[{player_three}]: Попытайтесь снова, у вас {mistake} попытки')
                    motion = int(input())
                    mistake -= 1
                else:
                    return print(f'[{player_three}]: Вы исчерпали свои попытки! Конец игры!')
            sum = sum + motion
        candies[0] = candies[0] - motion
        if candies[0] > 0:
            print(f'[{player_three}]: На кону {candies[0]} конфет')
        else:
            if candies[0] == 0:
                print(
                    f"Выиграл {player_one}! Выигранные {player_two}ом конфеты в количестве {number_of_candies - sum} также забирает победитель!")
            else:
                print(
                    f"Выиграл {player_two}! Выигранные {player_one}ом конфеты в количестве {sum} также забирает победитель!")
        cnt += 1


players = acquaintance()
candies = quantity_and_random(players)
the_game_itself(candies, players, bot_responses)