import logger as lg
import user_interface as ui
import real_numbers as rn
import complex_numbers as cn


def frac_trans(value):
    st = value.split('/')
    st1 = st[0].split()
    return f'{st[0].strip()}/{st[1].strip()}' if len(st1) == 1 else f'{st1[0].strip()} {st1[1].strip()}/{st[1].strip()}'


def calculation(number_one, number_second, number_action):
    lg.info_data(f'{number_one} {number_action} {number_second}')

    if ui.if_floating(number_one) and ui.if_floating(number_second):
        number_one = (float(number_one),)
        number_second = (float(number_second),)
        return rn.calculation(number_one, number_second, number_action)

    if ui.if_fractional(number_one) and ui.if_fractional(number_second):
        number_one = frac_trans(number_one)
        number_second = frac_trans(number_second)
        return rn.calculation(number_one, number_second, number_action)

    if ui.if_complex(number_one) and ui.if_complex(number_second):
        number_one = str(complex(number_one))
        number_second = str(complex(number_second))
        return cn.calculation(number_one, number_second, number_action)