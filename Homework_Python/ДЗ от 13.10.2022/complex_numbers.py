def calculation(number_one='', number_two='', action=''):

    first_input = complex(number_one)
    second_input = complex(number_two)

    if action == '+':
        result = str(first_input + second_input)
        return result
    elif action == '-':
        result = str(first_input - second_input)
        return result
    elif action == '*':
        result = str(first_input * second_input)
        return result
    elif action == '/':
        if action == '/' and number_two == '0':
            return "На ноль делить нельзя!"
        else:
            result = str(first_input / second_input)
            return result