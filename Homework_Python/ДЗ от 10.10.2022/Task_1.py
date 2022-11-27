# Задача 1. Создайте программу для игры в "Крестики-нолики".

matrix = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def print_board(condition):
    for i, a in enumerate(condition):
        if (i+1) % 3 == 0:
            print(f'{a}')
        else:
            print(f'{a}|', end='')


print_board(matrix)

winning_cells = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def determine_winner(matrix, winning_cells):
    winning = ""

    for i in winning_cells:
        if matrix[i[0]] == "X" and matrix[i[1]] == "X" and matrix[i[2]] == "X":
            winning = "X"
        if matrix[i[0]] == "O" and matrix[i[1]] == "O" and matrix[i[2]] == "O":
            winning = "O"

    return winning


def game_state(matrix):
    symbol_status = 'X'
    while (determine_winner(matrix, winning_cells) == ''):
        index = int(input(f'В какой ячейке нарисовать {symbol_status}: '))
        matrix[index] = symbol_status

        print_board(matrix)

        winner_sign = determine_winner(matrix, winning_cells)
        if winner_sign != '':
            print(f'Победу одержал {winner_sign}')
        symbol_status = 'X' if symbol_status == 'O' else 'O'


game_state(matrix)