def ent_type(mark):
    global type_selection
    choice = True
    while choice:
        choice = True
        type_selection = input(
            'Какое число будете вводить? Нажмите в, если вещественное, и к - если комплексное: ').lower()
        if type_selection in ('в', 'к'):
            choice = False
        elif mark == 1:
            type_selection = 'в'
        elif mark == 2:
            type_selection = 'к'
        else:
            type_selection = 'Недопустимое значение'
        return type_selection


def if_floating(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def if_fractional(value):
    wf = value.split('/')
    if len(wf) != 2:
        return False
    if wf[0].replace(' ', '0').replace('-', '0').isdigit() and wf[1].replace(' ', '0').isdigit():
        return True
    else:
        return False


def if_complex(value):
    try:
        complex(value)
        if complex(value).imag == 0:
            return False
        else:
            return True
    except ValueError:
        return False


def ent_data(chck):
    global input_value
    chck = True
    while (chck):
        chck = True
        if type_selection == 'в':
            input_value = input(
                'Введите число, отделив дробную часть точкой: ')
            if if_floating(input_value) or if_fractional(input_value):
                chck = False
            else:
                print('Нужно ввести число')
        if type_selection == 'к':
            input_value = input('Значение комплексного числа a + bj: ')
            if if_complex(input_value):
                chck = False
            else:
                print('Число не является комплексным')

    return input_value


def ent_action(chck):
    global math_action
    act = ['+', '-', '*', '/']
    chck = True
    while (chck):
        chck = True
        math_action = input('Введите действие над числами (+, -, *, /): ')
        if math_action in act:
            chck = False

    return math_action


def rec_result(mark, data):
    print(data)
    with open('log.txt', 'a') as rs:
        rs.write(f'{data}\n')
    return data


def menu_amount(mark):
    ent_type(mark)
    return (ent_data(mark), ent_data(mark), ent_action(mark))