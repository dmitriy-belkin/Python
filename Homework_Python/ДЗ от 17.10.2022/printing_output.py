import easygui
from easygui import *


def printing_out(data):
    if len(data) > 0:
        msgbox(data)
    else:
        print("Журнал пуст!")