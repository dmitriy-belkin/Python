# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ИГРА ЧЕЛОВЕК ПРОТИВ ЧЕЛОВЕКА

import random
from random import randint
from random import choice


def acquaintance():
    global player_one, player_two, player_three
    player_three = 'Крупье'
    player_two = input(f'[{player_three}]: Первый игрок, ваше имя: ')
    player_one = input(f'[{player_three}]: Второй игрок, ваше имя: ')
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
        if cnt % 2 != 0:
            print(f'[{player_three}]: {players[1]}, {choice(bot_responses)}')
            motion = int(input())
            if motion == 1 or motion == 21:
                print(f'[{player_two}]: Готов забрать {motion} конфету')
            elif 2 <= motion < 5 or motion == 22 or motion == 23 or motion == 2:
                print(
                    f'[{player_two}]: Не будете возражать, если я возьму {motion} конфеты?')
            else:
                print(f'[{player_two}]: Пододвигаю к себе {motion} конфет')
        else:
            print(f'[{player_three}]: {players[0]}, {choice(bot_responses)}')
            motion = int(input())
            if motion == 1 or motion == 21:
                print(f'[{player_one}]: Я беру {motion} конфету')
            elif 2 <= motion < 5 or motion == 22 or motion == 23 or motion == 2:
                print(f'[{player_one}]: Мои {motion} конфеты')
            else:
                print(f'[{player_one}]: Извините, забираю {motion} конфет')

        if motion > candies[0] or motion > candies[1]:
            print(f'[{player_three}]: Вы можете взять не более {candies[1]} конфет')
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
        sum += motion
        candies[0] -= motion
        if candies[0] > 0:
            print(f'[{player_three}]: На кону {candies[0]} конфет')
        else:
            if candies[0] == 0:
                print(
                    f"Выиграл {player_one}! Выигранные {player_two}ом конфеты в количестве {number_of_candies - sum} штук также забирает победитель!")
            else:
                print(
                    f"Выиграл {player_two}! Выигранные {player_one}ом конфеты в количестве {sum} штук также забирает победитель!")
        cnt += 1


players = acquaintance()
candies = quantity_and_random(players)
the_game_itself(candies, players, bot_responses)