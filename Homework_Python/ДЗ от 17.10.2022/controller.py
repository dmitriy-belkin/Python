import easygui
from easygui import *
from export_data_user import *
from import_data_user import *
from printing_output import *
from search_data_user import *
import class_data as cad


def input_data():

    msg = 'Заполните все данные'
    title = None
    fieldNames = ['ID', 'Фамилия', 'Имя', 'Дата рождения', 'Успеваемость']
    fieldValues = multenterbox(msg, title, fieldNames)
    ID = fieldValues[0]
    last_name = fieldValues[1]
    first_name = fieldValues[2]
    date_of_birth = fieldValues[3]
    academic_performance = fieldValues[4]
    return [ID, last_name, first_name, date_of_birth, academic_performance]


message = ['Внести в журнал данные на ученика',
           'Вывести на экран журнал', 'Поиск ученика']


def choice_todo():

    mes = list(message)
    ch = easygui.choicebox(msg='Выберите действие', title='', choices=mes)

    if ch == 'Внести в журнал данные на ученика':
        export_data_user(input_data())
    elif ch == 'Вывести на экран журнал':
        data = import_data_user()
        printing_out(data)
    else:
        msg = 'Введите данные для поиска'
        title = 'Вопрос'
        fieldNames = ['Фамилия']
        fieldValues1 = multenterbox(msg, title, fieldNames)
        word = fieldValues1[0]
        data = import_data_user()
        item = search_data_user(word, data)
        if item != None:
            msg = (
                f'ID: {item[0]}, Фамилия: {item[1]}, имя: {item[2]}, год рождения: {item[3]}, успеваемость: {item[4]}')
            msgbox(msg)
        else:
            msgbox("Данные не обнаружены")


def office():
    msg = 'Введите ID студента для вывода его данных по классу'
    title = 'Вопрос'
    fieldNames = ['ID']
    fieldValues = multenterbox(msg, title, fieldNames)
    ID = fieldValues[0]
    if ID in cad.student_data['ID']:
        index = cad.student_data['ID'].index(ID)
        msgbox(
            f" Сидит в кабинете {cad.student_data['Предмет'][index]}, {cad.student_data['Ряд'][index]}, за партой номер {cad.student_data['Вариант'][index]}, {cad.student_data['Вид парты'][index]}")