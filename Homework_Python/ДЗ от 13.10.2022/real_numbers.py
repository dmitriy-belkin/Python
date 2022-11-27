def calculation(x, y, action):
    if type(x) == str and type(y) == str:
        if x.find('/') < 0 and y.find('/') < 0:
            ax = float(x)
            bx = float(y)
            return operation(ax, bx, action)
        else:
            if x[x.find('/') + 1] == '0' or y[y.find('/') + 1] == '0':
                return 'На ноль делить нельзя!'
    if type(x) == tuple and type(y) == tuple:
        ax = float(x[0])
        bx = float(y[0])
        return operation(ax, bx, action)


def operation(a, b, action):
    operation_action = max(
        len(str(a).split('.')[1]), len(str(b).split('.')[1]))


    if action == '+':
        return str(round(a + b, operation_action))
    elif action == '-':
        return str(round(a - b, operation_action))
    elif action == '*':
        return str(round(a * b, operation_action))
    elif action == '/':
        if b != 0:
            return str(round(a / b, operation_action))
        else:
            print('На ноль делить нельзя!')