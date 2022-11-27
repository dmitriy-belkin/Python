# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def string_encoding(string):
    empty_string = ''
    output_string = ''
    cnt = 1
    if not string:
        return ''
    for char in string:
        if char != output_string:
            if output_string:
                empty_string += str(cnt) + output_string
            cnt = 1
            output_string = char
        else:
            cnt += 1
    else:
        empty_string += str(cnt) + output_string
        return empty_string


def string_decoding(string):
    decoding = ''
    cnt = ''
    for char in string:
        if char.isdigit():
            cnt += char
        else:
            decoding += char * int(cnt)
            cnt = ''
    return decoding


string = input('Enter the text: ')
print(f'Encrypted text: {string_encoding(string)}')
print(f'Decrypted text: {string_decoding(string_encoding(string))}')

with open('string_encoding.txt', 'w', encoding='UTF-16') as encod:
    encod.writelines(string_encoding(string))

with open('string_decoding.txt', 'w', encoding='UTF-16') as decod:
    decod.writelines(string_decoding(string_encoding(string)))